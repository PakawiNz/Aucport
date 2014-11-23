from django.shortcuts import render
from mainapp import models,common

@common.gen_view('Advance Search','product/search.html')
def form(request):
	context = {
		'categorys':models.Category.objects.all(),
	}
	return context
	
@common.gen_view('Product List','product/searchlist.html',postOnly=True)
def search(request) :
	name = request.POST.get('name')
	brand = request.POST.get('brand')
	category = request.POST.get('category')
	lprice = request.POST.get('lprice')
	hprice = request.POST.get('hprice')

	result = models.Product.objects.filter(state=models.Product.STATE_PENDING)
	if category : result = result.filter(category=category)
	if name : result = result.filter(name__contains=name)
	if brand : result = result.filter(brand__contains=brand)
	if lprice : result = result.filter(netPrice__gte=lprice)
	if hprice : result = result.filter(netPrice__lte=hprice)

	context = {
		'products':result,
	}
	return context