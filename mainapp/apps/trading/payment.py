from django.shortcuts import render
from mainapp import models,common

def clean(product,viewer) :
	if product.owner == viewer :
		raise Exception("Sorry. You can't purchase your own product.")
	elif product.state == product.STATE_AUCTION :
		raise Exception("Sorry. The Auction is still on progress.")
	elif product.state == product.STATE_SELLING  :
		pass
	elif product.state == product.STATE_BILLING  :
		auction = models.get_one(models.Auction,bidder=viewer,product=product)
		if not auction or product.highest_auction != auction :
			raise Exception("Sorry. You have no right to purchase this product.")
	else :
		raise Exception("Sorry. This Product is not available.")

@common.gen_view('Payment','trading/payment.html',memberOnly=True)
def main(request,pid):
	viewer = common.getLoginMember(request)
	product = models.Product.objects.get(id=pid)
	clean(product, viewer)

	context = {
		'product':product,
	}
	return context

@common.gen_view('Payment Result','common/success.html',memberOnly=True,postOnly=True)
def payment(request):
	viewer = common.getLoginMember(request)
	cardid = request.POST.get('creditcard')
	product = request.POST.get('product')

	if cardid != "0000111122223333" :
		raise Exception("Sorry. Your CreditCard is not available.")

	creditcard = models.get_one(models.CreditCard,cardid=cardid,owner=viewer)
	if not creditcard :
		creditcard = models.CreditCard(cardid=cardid,owner=viewer)
		creditcard.save()

	product = models.Product.objects.get(id=product)
	clean(product, viewer)

	transaction = models.Transaction(
		product=product,
		buyer=viewer,
		card=creditcard,)

	transaction.save()

	product.state = product.STATE_SOLDOUT
	product.save()

	context = {
		'content':'Transaction complete',
	}
	return context