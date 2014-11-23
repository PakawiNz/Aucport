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

@common.gen_view('Profile Update','member/register.html',memberOnly=True)
def edit(request):
	context = {
		'member': common.getLoginMember(request),
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	return context

@common.gen_view(guestOnly=True,postOnly=True,redirect=True)
def register(request):

	result = clean(request, True)
	if result != True :
		return result

	context = { 'content':
		"Successfully Registered : You should click the link in your email to confirm, blah blah blah"}
	return render(request,'common/success.html',context)

@common.gen_view(memberOnly=True,postOnly=True,redirect=True)
def update(request):

	result = clean(request, False)
	if result != True :
		return result

	context = { 'content':
		"Successfully Updated : ei ei ei"}
	return render(request,'common/success.html',context)

def clean(request,isRegister):
	email = request.POST.get('email')
	password = request.POST.get('password')
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	displayname = request.POST.get('displayname')
	birthdate = request.POST.get('birthdate')
	phone = request.POST.get('phone')
	address = request.POST.get('address')
	country = request.POST.get('country')
	timezone = request.POST.get('timezone')
	picture = request.FILES.get('picture')

	oldpassword = request.POST.get('oldpassword')
	password_confirmation = request.POST.get('password_confirmation')
	agreement = request.POST.get('agreement')

	errorList = {}

	if password_confirmation != password :
		errorList['password_confirmation'] = ['Confirmation Password Not Match']
	try : 
		birthdate = datetime.datetime.strptime(birthdate,"%d %b %Y")
	except : 
		birthdate = datetime.datetime.now().replace(year=2000)
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

	context = {}

	if isRegister :
		if not agreement :
			errorList['agreement'] = ['You should agree to the Terms and Conditions']

		confirm = hashlib.sha224(email+password).hexdigest()

		member = models.Member(
			email=email,password=password,
			firstname=firstname,lastname=lastname,
			displayname=displayname,birthdate=birthdate,
			phone=phone,address=address,
			country=country,timezone=timezone,
			picture=picture,confirmation=confirm)
	else :
		member = common.getLoginMember(request)

		if password : 
			if oldpassword != member.password :
				errorList['oldpassword'] = ['Old Password Not Match']
			member.password = password
		if firstname : member.firstname = firstname
		if lastname : member.lastname = lastname
		if displayname : member.displayname = displayname
		if birthdate : member.birthdate = birthdate
		if phone : member.phone = phone
		if address : member.address = address
		if country : member.country = country
		if timezone : member.timezone = timezone
		if picture : member.picture = picture

	try :
		member.full_clean()
	except Exception as e :
		for error in e.args :
			if not error : continue
			for field,exceptions in error.items() :
				errorList[field] = errorList[field] if errorList.get(field) else []
				for exception in exceptions :
					errorList[field].append(unicode(exception.message))

	if not request.POST.get('isSubmit') :
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

	if isRegister :
		confirm_url = "http://127.0.0.1:8000/member/confirm?email=" + email + "&confirm=" + confirm
		common.sendmail("Aucport : Email Confirmation", "Please Click This Link : " + confirm_url, [email])

	return True
