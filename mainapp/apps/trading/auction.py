from django.shortcuts import render
import datetime
from mainapp import models


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
		'title': 'Auction watchlist',
		'today':datetime.datetime.now(),
		'auctions':auctions,
	}
	return render(request,'trading/auction.html',context)

def bid(request) :
	if not request.POST :
		return render(request,'common/invalid.html')

	formstate = request.POST

	request_product = formstate.get('product')
	product_list = models.Product.objects.filter(id=request_product)

	if product_list :
		product = product_list[0]
		auction = product.highest_auction


	if formstate.get('')
	if amount == 0 :
		if self.product.netPrice < self.ceiling :
			self.current = min([self.current + self.increase, self.ceiling])
			self.product.netPrice = self.current
			self.lastbid = datetime.datetime.now()
		else :
			self.isAuto = False
			if self.notify :
				common.sendmail("Aucport : Auction Notificaton", "", [self.bidder.email])
	else :
		if self.product.netPrice < amount :
			self.current = amount
			self.product.netPrice = self.current
			self.lastbid = datetime.datetime.now()
		else :
			return False