from django.shortcuts import render,redirect
from mainapp import models

def invalid() :
	return render(request,'common/invalid.html',{'content':'No Member Information'})

def main(request):
	if not request.GET : 
		member = request.session.get('member')
		if member :
			return redirect('/member/profile?member='+str(member))
		return invalid()

	member = request.GET.get('member')
	if not member : return invalid()

	member = models.Member.objects.filter(id=member)
	if not member : return invalid()

	member = member[0]

	context = {
		'member':member,
		'buy':models.Transaction.objects.filter(buyer=member).count(),
		'sell':models.Transaction.objects.filter(product__in=models.Product.objects.filter(owner=member)).count(),
		'liked':0,
	}
	return render(request,'member/profile.html',context)