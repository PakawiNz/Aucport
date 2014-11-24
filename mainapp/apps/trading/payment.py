from django.shortcuts import render
from mainapp import models,common

@common.gen_view('Payment','trading/payment.html',memberOnly=True)
def main(request,pid):
	product = models.Product.objects.get(id=pid)
	if product.owner == common.getLoginMember(request) :
		raise Exception("Sorry. You can't purchase your own product.")
	context = {
		'product':product,
	}
	return context