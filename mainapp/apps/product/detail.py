from django.shortcuts import render
from mainapp import models,common

@common.gen_view('Product Detail','product/detail.html')
def show(request):
	return {}

@common.gen_view('Edit Product Detail','product/editdetail.html',memberOnly=True,postOnly=True)
def edit(request):
	return {}