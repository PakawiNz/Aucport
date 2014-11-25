from django.shortcuts import render
from mainapp import models,common


@common.gen_view('Profile','member/profile.html',memberOnly=True,redirect=True)
def owner(request):
	viewer = models.get_one(models.Member,id=request.session.get('member'))
	return show(request,viewer.id)
	
@common.gen_view('Profile','member/profile.html')
def show(request,mid):
	viewer = models.get_one(models.Member,id=request.session.get('member'))
	member = models.get_one(models.Member,id=mid)
	if not member : raise Exception("No Member with such ID.")

	context = {
		'title': member.displayname,
		'hideTitle': True,
		'member':member,
		'products':models.Product.objects.filter(owner=member),
		'products_wait':models.Product.objects.filter(owner=member,state=models.Product.STATE_BILLING),
		'buy':models.Transaction.objects.filter(buyer=member).count(),
		'sell':models.Transaction.objects.filter(product__in=models.Product.objects.filter(owner=member)).count(),
		'like':0,
		'dislike':0,
		'isOwner':viewer == member,
	}
	return context

@common.gen_view('Edit Profile','member/editprofile.html',memberOnly=True)
def edit(request):
	context = {
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	return context