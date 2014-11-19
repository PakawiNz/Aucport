from django.shortcuts import render
from mainapp import models,common

def main(request):
	if request.POST : return search(request)
	context = {
		'title':'Advance Search',
	}
	common.gencontext(request, context)
	return render(request,'product/search.html', context)

def search(request) :

	context = {
		'title':'Product List',
		'subtitle':'with keyword blah blah',
	}
	common.gencontext(request, context)
	return render(request,'product/searchlist.html',context)