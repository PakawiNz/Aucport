from django.core.mail import send_mail
from django.conf import settings
from mainapp import models

def gencontext(request,context):

	member = request.session.get('member')
	if not member : return

	member = models.Member.objects.filter(id=member)
	if not member : return

	member = member[0]

	context['member'] = member

def sendmail(title,content,receipants):
	send_mail(title, content, settings.EMAIL_HOST_USER, receipants)
