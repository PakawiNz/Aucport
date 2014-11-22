from django.shortcuts import render,render_to_response,redirect
from mainapp import models,common

def show(request):
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
		'hideTitle': True,
		'title': member.displayname,
		'member':member,
		'products':models.Product.objects.filter(owner=member),
		'buy':models.Transaction.objects.filter(buyer=member).count(),
		'sell':models.Transaction.objects.filter(product__in=models.Product.objects.filter(owner=member)).count(),
		'liked':0,
		'isOwner':viewer == member.id,
	}
	return render(request,'member/profile.html',context)


@common.gen_view('Edit Profile','member/editprofile.html',memberOnly=True)
def edit(request):
	context = {
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	return context