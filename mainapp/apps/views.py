from django.shortcuts import render
from mainapp import common, models

@common.gen_view('Home','home.html')
def home(request) :
	context = {
		'products':models.Product.objects.filter(),
	}
	return context