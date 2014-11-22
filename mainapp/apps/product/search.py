from django.shortcuts import render
from mainapp import models,common

@common.gen_view('Advance Search','product/search.html')
def form(request):
	return {}
	
@common.gen_view('Product List','product/searchlist.html',postOnly=True)
def search(request) :
	context = {
		'products':models.Product.objects.all(),
	}
	return context
