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