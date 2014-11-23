from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
	response = render_to_response('common/invalid.html', 
		{'content':'Sorry. This url does not provide service.'},
		 context_instance=RequestContext(request))
	response.status_code = 404
	return response

def handler500(request):
	response = render_to_response('common/invalid.html', 
		{'content':'Sorry. There is an error on our server.'},
		context_instance=RequestContext(request))
	response.status_code = 500
	return response