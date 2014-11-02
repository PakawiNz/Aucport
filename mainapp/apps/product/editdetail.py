from django.shortcuts import render

def main(request):
	return render(request,'product/editdetail.html')