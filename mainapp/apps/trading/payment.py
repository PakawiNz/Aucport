from django.shortcuts import render
from mainapp import models,common
import datetime

@common.gen_view('Transaction History','trading/history.html',memberOnly=True)
def history(request):
	viewer = common.getLoginMember(request)

	context = {
		'transactions':viewer.getMyTransaction(),
	}
	return context

@common.gen_view('Feedback','trading/feedback.html',memberOnly=True)
def feedback(request,tid):
	viewer = common.getLoginMember(request)
	transaction = models.Transaction.objects.get(id=tid)
	if transaction.buyer != viewer :
		raise Exception("Sorry. You can't comment on product you not buy.")
	if transaction.comment :
		raise Exception("Sorry. You've already comment on this product.")

	context = {
		'transaction':transaction,
	}
	return context

@common.gen_view('Feedback','trading/feedback.html',memberOnly=True,postOnly=True)
def dofeedback(request):
	viewer = common.getLoginMember(request)
	transaction = models.Transaction.objects.get(id=tid)
	if transaction.buyer != viewer :
		raise Exception("Sorry. You can't comment on product you not buy.")
	if transaction.commend :
		raise Exception("Sorry. You've already comment on this product.")

	context = {
		'transaction':transaction,
	}
	return context

@common.gen_view('Payment','trading/payment.html',memberOnly=True)
def main(request,pid):
	viewer = common.getLoginMember(request)
	product = models.Product.objects.get(id=pid)
	if product.owner == viewer :
		raise Exception("Sorry. You can't purchase your own product.")
	elif product.state == product.STATE_AUCTION :
		if product.expired < datetime.datetime.now() :
			product.state = product.STATE_BILLING
			product.save()
		else :
			raise Exception("Sorry. The Auction is still on progress.")
	elif product.state == product.STATE_SELLING :
		pass
	else :
		raise Exception("Sorry. This Product is not available.")

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

	creditcard = models.CreditCard.objects.filter(cardid=cardid,owner=viewer)
	if not creditcard :
		creditcard = models.CreditCard(cardid=cardid,owner=viewer)
		creditcard.save()

	product = models.Product.objects.get(id=product)
	if product.owner == viewer :
		raise Exception("Sorry. You can't purchase your own product.")
	elif product.state == product.STATE_BILLING :
		auction = models.get_one(models.Auction,bidder=viewer,product=product)
		if not auction or product.highest_auction != auction :
			raise Exception("Sorry. You have no right to purchase this product.")
	elif product.state == product.STATE_SELLING :
		pass
	else :
		raise Exception("Sorry. This Product is not available.")


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