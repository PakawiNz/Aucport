from django.shortcuts import render
from mainapp import common, models

@common.gen_view('Home','home.html')
def home(request) :
	context = {
		'products':models.Product.objects.filter(
			state__in=[models.Product.STATE_AUCTION,models.Product.STATE_SELLING]).order_by('-view'),
		'randomdot':range(36),
	}
	return context

@common.gen_view('ERROR 404','common/invalid.html',status_code=404)
def handler404(request):
	context = {'content':'Sorry. This url does not provide service.'}
	return context

@common.gen_view('ERROR 500','common/invalid.html',status_code=500)
def handler500(request):
	context = {'content':'Sorry. There is an error on our server.'}
	return context