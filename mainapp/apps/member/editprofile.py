from django.shortcuts import render
from mainapp import models,common
import datetime

def main(request):
	context = {
		'title':'Edit Profile',
		'countries': models.Country.objects.all(),
		'timezones': models.Timezone.objects.all(),
	}
	common.gencontext(request, context)
	return render(request,'member/editprofile.html', context)