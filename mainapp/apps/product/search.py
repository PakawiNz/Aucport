from django.shortcuts import render

def main(request):
	if request.POST : return search(request)
	context = {
		'title':'Advance Search',
	}
	return render(request,'product/search.html', context)

def search(request) :

	context = {
		'title':'Product List',
		'subtitle':'with keyword blah blah',
	}
	return render(request,'product/searchlist.html',context)