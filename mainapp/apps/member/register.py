from django.shortcuts import render

def main(request):
	context = {
		'title':'Register',
	}
	return render(request,'member/register.html',context)