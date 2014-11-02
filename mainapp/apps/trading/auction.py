from django.shortcuts import render
import datetime

def main(request):
	auctions = [{
		'product': "Battle Fury",
		'picture': "http://cdn.dota2.com/apps/dota2/images/items/bfury_lg.png",
		'endtime': datetime.datetime.now() + datetime.timedelta(-1,10),
		},{
		'product': "Aghanim's Sceptor",
		'picture': "http://cdn.dota2.com/apps/dota2/images/items/ultimate_scepter_lg.png",
		'endtime': datetime.datetime.now() + datetime.timedelta(0,10),
		},{
		'product': "Boot of travel",
		'picture': "http://cdn.dota2.com/apps/dota2/images/items/travel_boots_lg.png",
		'endtime': datetime.datetime.now() + datetime.timedelta(0,70),
		},{
		'product': "Desolator",
		'picture': "http://cdn.dota2.com/apps/dota2/images/items/desolator_lg.png",
		'endtime': datetime.datetime.now() + datetime.timedelta(1,10),
		},
	]

	for auction in auctions :
		auction['endmonth'] = auction['endtime'].strftime('%b')

	context = {
		'today':datetime.datetime.now(),
		'auctions':auctions,
	}
	return render(request,'trading/auction.html',context)