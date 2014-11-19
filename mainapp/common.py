from mainapp import models

def gencontext(request,context):

	member = request.session.get('member')
	if not member : return

	member = models.Member.objects.filter(id=member)
	if not member : return

	member = member[0]

	context['member'] = member