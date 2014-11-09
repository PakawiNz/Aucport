from django.shortcuts import render

def main(request):
	context = {
		'title':'Advance Search',
	}
	return render(request,'product/search.html', context)