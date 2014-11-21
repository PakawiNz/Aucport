from django.shortcuts import render
from mainapp import models,common
import traceback
import datetime
import hashlib

def main(request):
	if request.method == 'POST' :
		return register(request);

	context = {
		'title':'Register',
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	common.gencontext(request, context)
	return render(request,'member/register.html',context)

def register(request):
	formstate = request.POST

	email = formstate.get('email')
	password = formstate.get('password')
	password_confirmation = formstate.get('password_confirmation')
	first_name = formstate.get('first_name')
	last_name = formstate.get('last_name')
	display_name = formstate.get('display_name')
	birthdate = formstate.get('birthdate')
	address = formstate.get('address')
	country = formstate.get('country')
	timezone = formstate.get('timezone')
	agreement = formstate.get('agreement')
	picture = request.FILES.get('profilepic')

	vresults = []
	vresults.append(V.validate(email,
		V.V_is_unique(models.Member,'email'),
		V.V_isEmail(),))
	vresults.append(V.validate(password,
		V.V_len_more_than(8),))
	vresults.append(V.validate(first_name,
		V.V_alphabet(),))
	vresults.append(V.validate(last_name,
		V.V_alphabet(),))
	vresults.append(V.validate(display_name,
		V.V_is_unique(models.Member,'displayname'),
		V.V_len_more_than(4),
		V.V_name(),))
	vresults.append(V.validate(birthdate))
	vresults.append(V.validate(address))
	vresults.append(V.validate(country,V.V_is_in_DB(models.Country)))
	vresults.append(V.validate(timezone,V.V_is_in_DB(models.Timezone)))
	vresults.append(V.validate(picture,V.V_file_isJPG()))

	isCompleted = True
	errorList = []
	for vresult in vresults :
		if vresult != True :
			isCompleted = False
			# errorList.append(vresult)
			for error in vresult : errorList.append(error)

	if isCompleted :
		birthdate = datetime.datetime.strptime(birthdate,"%d %b %Y")
		country=models.Country.objects.get(id=country)
		timezone=models.Timezone.objects.get(id=timezone)
		confirm = hashlib.sha224(email+password).hexdigest()

		member = models.Member(
			email=email,password=password,
			firstname=first_name,lastname=last_name,
			displayname=display_name,confirmation=confirm,
			birthdate=birthdate,address=address,
			country=country,timezone=timezone,picture=picture)

		member.save()

		confirm_url = "http://127.0.0.1:8000/member/confirm?email=" + email + "&confirm=" + confirm
		# common.sendmail("Aucport : Email Confirmation", "Please Click This Link : " + confirm_url, [email])

	if isCompleted :
		context = { 'content':
			"Successfully Registered : You should click the link in your email to confirm, blah blah blah"}
		return render(request,'common/success.html',context)
	else :
		context = { 
			'content':"There're following error",
			'errorList': errorList,
		}
		return render(request,'common/invalid.html',context)
