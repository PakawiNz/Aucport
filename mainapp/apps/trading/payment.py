from django.shortcuts import render
from mainapp import models,common

@common.gen_view('Payment','trading/payment.html',memberOnly=True)
def main(request):
	return {}