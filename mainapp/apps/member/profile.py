from django.shortcuts import render,render_to_response,redirect
from mainapp import models,common

def main(request):
	viewer = request.session.get('member')

	if viewer : result = redirect('/member/profile?member='+str(viewer))
	else : result = render(request,'common/invalid.html',{'content':'No Member Information'})

	if not request.GET : 
		return result

	member = request.GET.get('member')
	if not member : return result

	member = models.Member.objects.filter(id=member)
	if not member : return result

	member = member[0]

	context = {
		'showmember':member,
		'buy':models.Transaction.objects.filter(buyer=member).count(),
		'sell':models.Transaction.objects.filter(product__in=models.Product.objects.filter(owner=member)).count(),
		'liked':0,
		'isOwner':viewer == member.id,
	}
	common.gencontext(request, context)
	return render(request,'member/profile.html',context)