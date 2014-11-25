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