from django.shortcuts import render

def main(request):
	print 'DAFUQ'
	return render(request,'product/editdetail.html')