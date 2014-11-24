from django.shortcuts import render,redirect
from mainapp import models,common
from django .http import HttpResponse
import datetime
from mainapp import models, common
import unicodedata

@common.gen_view('Auction Watchlist','trading/auction.html',memberOnly=True)
def main(request):
	viewer = common.getLoginMember(request)
	auctions = models.Auction.objects.filter(bidder=viewer)

	context = {
		'today':datetime.datetime.now(),
		'state':models.Product,
		'auctions':auctions,
	}
	return context

@common.gen_view(memberOnly=True,redirect=True,postOnly=True)
def getupdated(request) :
	pids = request.POST.get('pids')
	viewer = common.getLoginMember(request)
	products = models.Product.objects.filter(id__in=pids)

	products_dump = {}
	for product in products :
		products_dump[product.id] = {}
		products_dump[product.id]['maxprice'] = product.getMaxPrice()
		if product.highest_auction :
			products_dump[product.id]['king'] = product.highest_auction.bidder == viewer

	return common.jsonResponse({'products':products_dump})

@common.gen_view(memberOnly=True,redirect=True)
def watch(request,pid) :
	viewer = common.getLoginMember(request)
	product = models.Product.objects.get(id=pid)
	auction = models.get_one(models.Auction,product=product,bidder=viewer)

	if product.owner == viewer :
		raise Exception('Can not add your own product')

	if not auction :
		auction = models.Auction(product=product,bidder=viewer)
		auction.save()
	
	return redirect('auction')

@common.gen_view(memberOnly=True,postOnly=True,redirect=True)
def bid(request) :

	formstate = request.POST
	auction = formstate.get('auction')
	current = formstate.get('current')
	ceiling = formstate.get('ceiling')
	increase = formstate.get('increase')
	isAuto = formstate.get('isAuto')

	viewer = common.getLoginMember(request)

	errorList = {}

	if auction != None :
		auction = models.Auction.objects.get(id=auction)
		if not auction :
			return common.jsonResponse({'success':False,'error':'No Such Auction with this ID'})
	else :
		return common.jsonResponse({'success':False,'error':'No Auction Found.'})

	if current != None :
		current = float(current)
		product = auction.product
		possessor = product.highest_auction

		oldmaxprice = possessor.current if possessor != None else product.netPrice
		if current <= oldmaxprice :
			return common.jsonResponse({'success':False,'error':'Input is lower than current price'})
		else : 
			auction.current = current
			auction.save()
			product.highest_auction = auction
			product.save()
			return common.jsonResponse({'success':True,'newval':current,})

	elif ceiling != None : 
		ceiling = float(ceiling)
		if ceiling < 0 :
			return common.jsonResponse({'success':False,'error':'Input is lower than 0'})
		auction.ceiling = ceiling
		auction.save()
		return common.jsonResponse({'success':True,'newval':ceiling,})

	elif increase != None : 
		increase = float(increase)
		if increase < 0 :
			return common.jsonResponse({'success':False,'error':'Input is lower than 0'})
		auction.increase = increase
		auction.save()
		return common.jsonResponse({'success':True,'newval':increase,})

	else :
		return common.jsonResponse({'success':False,'error':'No Data Found.'})

	request_product = formstate.get('product')
	requester = request.session.get('member')

	requester_list = models.Member.objects.filter(id=requester)
	product_list = models.Product.objects.filter(id=request_product)

	requester = requester_list[0]
	if product_list[0]:
		product = product_list[0]
		auction_old = product.highest_auction
		auction_new = models.get_one(models.Auction,bidder=requester, product=product)

		if unicodedata.numeric(ceiling) < auction_new.ceiling:
			return jsonResponse()

		if not auction_new:
			print 'new_one'
			auction_new = models.Auction(product=request_product,
				bidder= requester,
				ceiling = ceiling,
				increase = increase,
				current = current,
				isAuto = isAuto,
				)
		else:
			if ceiling == '':
				ceiling = auction_new.ceiling
			if increase == '':
				increase = auction_new.increase
			if current == '':
				current = auction_new.current
			if isAuto == 'true':
				isAuto = True
			elif isAuto == 'false':
				isAuto = False
			print 'old_one'
			auction_new.ceiling = ceiling			
			if isAuto:
				auction_new.increase = increase			
				auction_new.current = current
			auction_new.isAuto = isAuto			

		auction_new.save()
		auction_new = models.get_one(models.Auction,bidder=requester, product=product)
		
		winner = 0 # 0: old bidder, 1: new bidder

		if not auction_old:
			winner = 1
		else:
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
		product.save();
	print 'yeahhhhh'
	# requester = request.session.get('member')
	# aucts = models.Auction.objects.filter(id=requester)
	# auctions = []
	# for i,a in enumerate(aucts) :
	# 	product = {
	# 		'a': a,
	# 		'product': a.product,
	# 		'picture': a.product.picture1,
	# 		'endtime': a.product.expired,
	# 	}
	# 	auctions.append(product)

	# for auction in auctions :
	# 	auction['endmonth'] = auction['endtime'].strftime('%b')

	# context = {
	# 	'today':datetime.datetime.now(),
	# 	'auctions':auctions,
	# }
	# print context
	# return context
	return jsonResponse('context')

def fight() :
	pass