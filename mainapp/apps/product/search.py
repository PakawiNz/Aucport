from django.shortcuts import render
from mainapp import models,common

@common.gen_view(redirect=True)
def main(request):
	if request.GET : return search(request)
	else : return form(request)

@common.gen_view('Advance Search','product/search.html')
def form(request):
	context = {
		'categorys':models.Category.objects.all(),
	}
	return context

@common.gen_view('Product List','product/searchlist.html')
def search(request) :
	name = request.GET.get('name')
	brand = request.GET.get('brand')
	category = request.GET.get('category')
	lprice = request.GET.get('lprice')
	hprice = request.GET.get('hprice')

	result = models.Product.objects.filter(state__in=[models.Product.STATE_AUCTION,models.Product.STATE_SELLING])
	if category : result = result.filter(category=category)
	if name : result = result.filter(name__contains=name)
	if brand : result = result.filter(brand__contains=brand)
	if lprice : result = result.filter(netPrice__gte=lprice)
	if hprice : result = result.filter(netPrice__lte=hprice)

	context = {
		'products':result,
	}
	return context