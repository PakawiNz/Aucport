from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from mainapp import models
import traceback
import json

def gen_view(
		title="",
		template="",
		memberOnly=False,
		guestOnly=False,
		postOnly=False,
		redirect=False,
		):

	def inner_decorator(inner_func):
		def wrapper(*args,**kwargs):
			request = args[0]
			context = {
				'title':title,
				}

			login_member = getLoginMember(request)
			context['login_member'] = login_member
			post_state = request.POST
			
			if memberOnly and not login_member:
				context['content'] = 'Sorry. This area is only for Member'
				return render(request,'common/invalid.html',context)

			if guestOnly and login_member:
				context['content'] = 'Sorry. This area is only for Guest'
				return render(request,'common/invalid.html',context)

			if postOnly and not post_state:
				context['content'] = 'Sorry. This area for resulting only'
				return render(request,'common/invalid.html',context)

			try :
				if redirect : 
					return inner_func(*args,**kwargs)
				else :
					view_context = inner_func(*args,**kwargs)
					context.update(view_context)
					return render(request,template,context)

			except Exception as e :
				print traceback.format_exc()
				context['content'] = e.message
				return render(request,'common/invalid.html',context)
			
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

def jsonResponse(data):
	return HttpResponse(json.dumps(data))
