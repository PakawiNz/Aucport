from django.shortcuts import render,redirect
from django.core.mail import send_mail
from mainapp import models
from mainapp import validator as V

def login(request):
	if not request.POST : return render(request,'common/invalid.html')
	email = request.POST.get('email')
	password = request.POST.get('password')
	member = models.Member.objects.filter(email=email,password=password)
	if member :
		request.session['member'] = member[0].id
		if member[0].isConfirmed == True :
			return redirect('/')
		else :
			return render(request,'common/invalid.html',{'content':"This account hasn't been confirmed"})
	else :
		return render(request,'common/invalid.html',{'content':'invalid username or password'})

def logout(request):
	request.session.clear()
	context = {'content':"You have been logged out."}
	return render(request,'common/success.html',context)

def confirm(request):
	if not request.GET : return render(request,'common/invalid.html')
	email = request.GET.get('email')
	confirm = request.GET.get('confirm')
	member = models.Member.objects.filter(email=email,confirmation=confirm)
	if member :
		member[0].isConfirmed = True
		member[0].save()
		context = {'content':"Congratulation. Your account has been confirmed."}
		return render(request,'common/success.html',context)
	else :
		context = {'content':"Invalid Email or Confirmation Key"}
		return render(request,'common/invalid.html',context)

