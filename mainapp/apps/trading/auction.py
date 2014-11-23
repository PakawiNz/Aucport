from django.shortcuts import render
from mainapp import models,common
from django .http import HttpResponse
import datetime
from mainapp import models, common


@common.gen_view('Auction Watchlist','trading/auction.html',memberOnly=True)
def main(request):
	# requester = request.session.get('member')
	# products = models.Auction.objects.filter(bidder=requester)
	requester = models.Member.objects.filter(email='mi_ni_gift_@hotmail.com')
	aucts = models.Auction.objects.all().filter(bidder=requester[0])
	auctions = []
	for i,a in enumerate(aucts) :
		product = {
			'a': a,
			'product': a.product,
			'picture': a.product.picture1,
			'endtime': a.product.expired,
		}
		auctions.append(product)

	

	for auction in auctions :
		auction['endmonth'] = auction['endtime'].strftime('%b')

	context = {
		'today':datetime.datetime.now(),
		'auctions':auctions,
	}
	return context


def bid(request) :
	if not request.POST :
		return render(request,'common/invalid.html')
	print 'here<<<<<<<<<<<<<<<<<<<<< '
	formstate = request.POST

	request_product = formstate.get('product')
	requester = request.session.get('member')
	print requester
	requester_list = models.Member.objects.filter(email=requester)
	product_list = models.Product.objects.filter(name=request_product)

	requester = requester_list[0]

	if product_list:
		product = product_list[0]
		auction_old = product.highest_auction
		auction_new = common.getone(models.Auction,bidder=requester, product=product)
		if not auction_new:
			models.Auction(product=request_product,
				bidder=requester,
				ceiling = formstate.ceiling,
				increase = formstate.increase,
				current = formstate.amount,
				isAuto = formstate.isAuto,
				)

		winner = 0 # 0: old bidder, 1: new bidder

		if not auction_new.isAuto : # the bid request is in manual mode
			if not auction_old.isAuto : # The current highest bidder is manual bidding
				if auction_new.current > auction_old.current : # challenger wins
					winner = 1

				elif auction_new.current <= auction_old.current : # old bidder wins
					winner = 0

			else : # The current highest bidder is auto bidding
				if auction_new.current > auction_old.ceiling : # challenger wins
					winner = 1

				elif auction_new.current <= auction_old.ceiling : # old bidder wins
					while auction_old.current <= auction_new.current:
						auction_old.current += auction_old.increase
						winner = 0

		elif auction_new.current == 0 :# the bid request is in auto mode
			if not auction_old.isAuto : # The current highest bidder is manual bidding
				if auction_new.ceiling > auction_old.current : # challenger wins
					winner = 1
					auction_new.current = auction_old.current+auction_new.increase
				elif auction_new.ceiling <= auction_old.current : # old bidder wins
					winner = 0
			else : # The current highest bidder is auto bidding
				# Fight to determine winner
				bidder_turn = 1 # 0 = old bidder, 1 = challenger
				while True :
					if bidder_turn == 1 and auction_new.ceiling > auction_old.current :
						winner = 1
						auction_new.current = auction_old.current + auction_new.increase
						bidder_turn = 0
					elif bidder_turn == 0 and auction_old.ceiling > auction_new.current :
						winner = 0
						auction_old.current = auction_new.current + auction_old.increase
						bidder_turn = 1

		if winner == 0 :
			product.highest_auction = auction_old
		else :
			product.highest_auction = auction_new
	return HttpResponse('Success')
