from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from mainapp import models

def gen_view(title,template,
		memberOnly=False,
		guestOnly=False,
		postOnly=False,):

	def inner_decorator(inner_func):
		def wrapper(request):
			context = {
				'title':title,
				}

			login_member = getLoginMember(request)
			context['login_member'] = login_member
			post_state = request.POST
			
			if memberOnly and not getLoginMember:
				context['content'] = 'Sorry. This area is only for Member'
				return render(request,'common/invalid.html',context)

			if guestOnly and getLoginMember:
				context['content'] = 'Sorry. This area is only for Guest'
				return render(request,'common/invalid.html',context)

			if postOnly and not post_state:
				context['content'] = 'Sorry. This area for resulting only'
				return render(request,'common/invalid.html',context)

			view_context = inner_func(request)
			context.update(view_context)
			return render(request,template,context)
			
		return wrapper
	return inner_decorator

def getLoginMember(request):
	member = request.session.get('member')
	if not member : return None

	member = models.Member.objects.filter(id=member)
	if not member : return None

	return member[0]

def sendmail(title,content,receipants):
	send_mail(title, content, settings.EMAIL_HOST_USER, receipants)
