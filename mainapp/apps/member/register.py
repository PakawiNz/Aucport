from django.shortcuts import render
from mainapp import models,common
import traceback
import datetime
import hashlib

@common.gen_view('Register','member/register.html',guestOnly=True)
def main(request):
	context = {
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	return context

@common.gen_view(guestOnly=True,postOnly=True,redirect=True)
def register(request):

	formstate = request.POST
	email = formstate.get('email')
	password = formstate.get('password')
	firstname = formstate.get('firstname')
	lastname = formstate.get('lastname')
	displayname = formstate.get('displayname')
	birthdate = formstate.get('birthdate')
	phone = formstate.get('phone')
	address = formstate.get('address')
	country = formstate.get('country')
	timezone = formstate.get('timezone')
	picture = request.FILES.get('picture')
	submit = formstate.get('isSubmit')

	password_confirmation = formstate.get('password_confirmation')
	agreement = formstate.get('agreement')

	errorList = {}

	if not agreement :
		errorList['agreement'] = ['You should agree to the Terms and Conditions']
	if password_confirmation != password :
		errorList['password_confirmation'] = ['Confirmation Password Not Match']
	try : 
		birthdate = datetime.datetime.strptime(birthdate,"%d %b %Y")
	except : 
		birthdate = datetime.datetime.now()
		errorList['birthdate'] = ['This Birthdate is not valid format (should be like 11 Dec 2001)']
	try : 
		country=models.Country.objects.get(id=country)
	except : 
		country=models.Country.objects.first()
		errorList['country'] = ['This Country is not in Database']
	try : 
		timezone=models.Timezone.objects.get(id=timezone)
	except : 
		timezone=models.Timezone.objects.first()
		errorList['timezone'] = ['This Timezone is not in Database']

	confirm = hashlib.sha224(email+password).hexdigest()

	member = models.Member(
		email=email,password=password,
		firstname=firstname,lastname=lastname,
		displayname=displayname,birthdate=birthdate,
		phone=phone,address=address,
		country=country,timezone=timezone,
		picture=picture,confirmation=confirm)

	context = {}

	try :
		member.full_clean()
	except Exception as e :
		for error in e.args :
			if not error : continue
			for field,exceptions in error.items() :
				errorList[field] = errorList[field] if errorList.get(field) else []
				for exception in exceptions :
					errorList[field].append(unicode(exception.message))


	if not submit :
		if errorList :
			context['errorList'] = errorList
		else :
			context['success'] = True
		return common.jsonResponse(context)
	
	if errorList :
		errorListText = []
		for field,error in errorList.items() :
			errorListText.append("%s :: %s"%(field,", ".join(error)))

		context['errorList'] = errorListText
		context['content'] = "Validation Error."
		return render(request,'common/invalid.html',context)

	member.save()
	confirm_url = "http://127.0.0.1:8000/member/confirm?email=" + email + "&confirm=" + confirm
	common.sendmail("Aucport : Email Confirmation", "Please Click This Link : " + confirm_url, [email])
	context = { 'content':
		"Successfully Registered : You should click the link in your email to confirm, blah blah blah"}
	return render(request,'common/success.html',context)
