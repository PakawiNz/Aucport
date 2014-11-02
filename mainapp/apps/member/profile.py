from django.shortcuts import render

def main(request):
	return render(request,'member/profile.html')