from django.shortcuts import render
from mainapp import models,common
import traceback
import datetime
import hashlib

@common.gen_view('Register','member/register.html',guestOnly=True)
def main(request):
	if request.method == 'POST' :
		return register(request);

	context = {
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	return context

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

	member.clean()

	if isCompleted :
		member.save()
		confirm_url = "http://127.0.0.1:8000/member/confirm?email=" + email + "&confirm=" + confirm
		context = { 'content':
			"Successfully Registered : You should click the link in your email to confirm, blah blah blah"}
		return render(request,'common/success.html',context)
	else :
		context = { 
			'content':"There're following error",
			'errorList': errorList,
		}
		return render(request,'common/invalid.html',context)
