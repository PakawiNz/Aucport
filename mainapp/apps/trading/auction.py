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
	requester_list = request.session.get('member')
	requester_list = models.Member.objects.filter(id=requester)
	product_list = models.Product.objects.filter(id=request_product)

	# auction_new = models.Auction.objects.filter(id)




	if product_list:
		product = product_list[0]
		requester = requester_list[0]
		auction = product.highest_auction

		if formstate.amount != 0 :# the bid request is in manual mode
			if not auction.isAuto :# The current highest bidder is manual bidding
				if formstate.amount > auction.current : # challenger wins
					auction.bidder = requester
					# auction.ceiling
					# auction.increase
					auction.current = formstate.increase
					auction.isAuto = False
					# auction.notify
					# auction.lastbid

				elif formstate.amount <= auction.current : # old bidder wins
					# do nothing
					pass
			else auction.isAuto : # The current highest bidder is auto bidding
				if formstate.amount > auction.ceiling : # challenger wins
					auction.bidder = requester
					# auction.ceiling
					# auction.increase
					auction.current = formstate.increase
					auction.isAuto = False
					# auction.notify
					# auction.lastbid
				elif formstate.amount <= auction.ceiling : # old bidder wins
					while auction.current <= formstate.amount:
						auction.current += auction.increase
						pass

		elif formstate.amount == 0 # the bid request is in auto mode
			if not auction.isAuto # The current highest bidder is manual bidding
				if formstate.ceiling > auction.current : # challenger wins
					auction.bidder = requester
					auction.ceiling = formstate.ceiling
					auction.increase = formstate.increase
					auction.current += formstate.increase
					auction.isAuto = True
					# auction.notify
					# auction.lastbid
				elif formstate.ceiling <= auction.current : # old bidder wins
					# do nothing
					pass
			else auction.isAuto # The current highest bidder is auto bidding
				# Fight to determine winner
				bidder_turn = 0 # 0 = challenger, 1 =  old bidder
				highest_bidder = auction.bidder
				highest_ceiling = auction.ceiling
				highest_increase = auction.increase
				highest_current = auction.current
				while auction.ceiling > highest_current and formstate.ceiling > highest_current:
					if bidder_turn == 0 :
						highest_bidder = requester
						highest_ceiling = formstate.ceiling
						highest_increase = formstate.increase
						highest_current += formstate.increase
						# auction.isAuto
						# auction.notify
						# auction.lastbid
						bidder_turn = 1
					else :
						highest_bidder = auction.bidder
						highest_ceiling = auction.ceiling
						highest_increase = auction.increase
						highest_current += auction.increase
						# auction.isAuto
						# auction.notify
						# auction.lastbid
						bidder_turn = 0
					pass
		
				auction.bidder = highest_bidder
				auction.ceiling = highest_ceiling
				auction.increase = highest_increase
				auction.current = highest_current


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