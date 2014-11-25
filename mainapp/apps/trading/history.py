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

def clean(transaction,viewer,request=None):

	if transaction.buyer != viewer :
		raise Exception("Sorry. You can't comment on product you not buy.")
	if transaction.comment :
		raise Exception("Sorry. You've already comment on this product.")
	if request :
		score = int(request.POST.get('score'))
		comment = request.POST.get('comment')
		critical = request.POST.get('critical')

		if critical == "true" :
			transaction.critical = True;
		elif critical == "false" :
			transaction.critical = False;
		else :
			raise Exception("Sorry. Critical value is invalid")
		if score > 5 or score < -5 :
			raise Exception("Sorry. Score value is invalid")

		transaction.score = score;
		transaction.comment = comment;
		transaction.save()

@common.gen_view('Feedback','trading/feedback.html',memberOnly=True)
def feedback(request,tid):
	viewer = common.getLoginMember(request)
	transaction = models.Transaction.objects.get(id=tid)
	clean(transaction, viewer)

	context = {
		'transaction':transaction,
	}
	return context

@common.gen_view('Feedback Result','common/success.html',memberOnly=True,postOnly=True)
def dofeedback(request):
	viewer = common.getLoginMember(request)
	transaction = models.Transaction.objects.get(id=request.POST.get('transaction'))
	clean(transaction, viewer, request)

	context = {
		'content':'Feedbacking Completed',
	}
	return context