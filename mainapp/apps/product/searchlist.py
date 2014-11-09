from django.shortcuts import render

def main(request):
	context = {
		'title': 'Product List',
	}
	return render(request,'product/searchlist.html',context)