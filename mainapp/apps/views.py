from django.shortcuts import render
from mainapp import common

@common.gen_view('Home','home.html')
def home(request) :
	return {}