from django.shortcuts import render,redirect
from mainapp import models,common
import datetime

@common.gen_view('Auction Watch List','trading/auction.html',memberOnly=True)
def main(request,unwatched=False):
	viewer = common.getLoginMember(request)
	auctions = models.Auction.objects.filter(bidder=viewer).order_by('-product__expired')
	auctions = auctions.filter(unwatched=unwatched)

	context = {
		'today':datetime.datetime.now(),
		'state':models.Product,
		'auctions':auctions,
	}
	if not unwatched :
		context['speclink'] = {'name':'Unwatched List','url':'/trading/auction_u/'}
	else :	
		context['speclink'] = {'name':'Watch List','url':'/trading/auction/'}
		context['title'] = 'Auction Unwatched List'

	return context

@common.gen_view(memberOnly=True,redirect=True)
def unwatched_list(request):
	return main(request,True)

@common.gen_view(memberOnly=True,redirect=True,postOnly=True)
def getupdated(request) :
	pids = request.POST.get('pids')
	viewer = common.getLoginMember(request)
	auctions = models.Auction.objects.filter(id__in=pids)

	products_dump = {}
	for auction in auctions :
		product = auction.product
		if product.isExpired() :
			if product.highest_auction :
				product.state = product.STATE_BILLING
			else : 
				product.state = product.STATE_PENDING
			product.save()

		products_dump[auction.id] = {}
		products_dump[auction.id]['isExpired'] = product.isExpired()
		products_dump[auction.id]['maxprice'] = product.getMaxPrice()
		products_dump[auction.id]['curprice'] = auctions.get(product=product).current
		if product.highest_auction :
			products_dump[auction.id]['king'] = product.highest_auction.bidder == viewer

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
	unwatched = formstate.get('unwatched')
	current = formstate.get('current')
	ceiling = formstate.get('ceiling')
	increase = formstate.get('increase')
	isAuto = formstate.get('isAuto')
	isNotify = formstate.get('isNotify')

	viewer = common.getLoginMember(request)

	errorList = {}

	if auction != None :
		auction = models.Auction.objects.get(id=auction)
		if not auction :
			return common.jsonResponse({'success':False,'error':'No Such Auction with this ID'})
	else :
		return common.jsonResponse({'success':False,'error':'No Auction Found.'})

	if unwatched != None :
		unwatched = int(unwatched)
		auction.unwatched = unwatched
		auction.save()
		return common.jsonResponse({'unwatched':unwatched,})

	if auction.product.isExpired() :
		return common.jsonResponse({'success':False,'error':"Auction's already expired."})

	if current != None :
		current = float(current)
		product = auction.product
		possessor = product.highest_auction

		oldmaxprice = product.getMaxPrice()
		if current <= oldmaxprice :
			return common.jsonResponse({'success':False,'error':'Input is lower than current price'})
		else : 
			auction.bid(current)
			auction.save()
			fight_man(auction)
			return common.jsonResponse({'success':True,'newval':current,})

	elif ceiling != None : 
		ceiling = float(ceiling)
		if ceiling < 0 :
			return common.jsonResponse({'success':False,'error':'Input is lower than 0'})
		auction.ceiling = ceiling
		auction.save()
		if auction.isAuto : fight_auto(auction)
		return common.jsonResponse({'success':True,'newval':ceiling,})

	elif increase != None : 
		increase = float(increase)
		if increase <= 0 :
			return common.jsonResponse({'success':False,'error':'Input must be more than 0'})
		auction.increase = increase
		auction.save()
		return common.jsonResponse({'success':True,'newval':increase,})
	elif isAuto != None : 
		if isAuto == True :
			auction.isAuto = True
			auction.save()
			fight_auto(auction)
		elif isAuto == False :
			auction.isAuto = False
			auction.save()
		else :
			return common.jsonResponse({'success':False,'error':'Invalid Auto.'})
		return common.jsonResponse({'success':True})
	elif isNotify != None : 
		if isNotify == True :
			auction.isNotify = True
			auction.save()
		elif isNotify == False :
			auction.isNotify = False
			auction.save()
		else :
			return common.jsonResponse({'success':False,'error':'Invalid Notify.'})
		return common.jsonResponse({'success':True})
	else :
		return common.jsonResponse({'success':False,'error':'No Data Found.'})

def fight_auto(auction) :
	product = auction.product
	possesor = product.highest_auction
	if auction == possesor : return
	if auction.ceiling <= product.getMaxPrice() : return
	if not possesor or not possesor.isAuto :
		auction.bid(min(auction.ceiling, product.getMaxPrice() + auction.increase))
		product.highest_auction = auction
	else :
		if auction.ceiling > possesor.ceiling :
			possesor.bid(possesor.ceiling)
			auction.bid(min(auction.ceiling, max(possesor.ceiling, product.getMaxPrice()) + auction.increase))
			product.highest_auction = auction
		elif auction.ceiling < possesor.ceiling :
			possesor.bid(min(possesor.ceiling, max(auction.ceiling, product.getMaxPrice()) + possesor.increase))
			auction.bid(auction.ceiling)
			product.highest_auction = possesor
		else :
			possesor.bid(possesor.ceiling)
			auction.bid(auction.ceiling)
		possesor.save()

	auction.save()
	product.save()

def fight_man(auction) :
	product = auction.product
	possesor = product.highest_auction
	if not possesor or not possesor.isAuto :
		product.highest_auction = auction
	else :
		if auction.current > possesor.ceiling :
			possesor.bid(possesor.ceiling)
			product.highest_auction = auction
		else :
			possesor.bid(min(possesor.ceiling, auction.current + possesor.increase))
		possesor.save()

	product.save()