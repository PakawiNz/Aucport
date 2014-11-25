from django.shortcuts import render,redirect
from mainapp import models,common
import datetime

class form(object) :
	def __init__(self,index,type,name,label,value,required) :
		self.index = index
		self.type = type
		self.name = name
		self.label = label
		self.value = value
		self.required = "required" if required else ""

@common.gen_view('','')
def dump(request):
	raise Exception("No Product ID found.")

@common.gen_view('Product Detail','product/detail.html')
def show(request,pid):
	product = models.Product.objects.get(id=pid)
	context = {
		'product':product,
	}
	return context

@common.gen_view('Create New Product','product/editdetail.html',memberOnly=True)
def create(request):
	forms = [
		form(0,'text','Name','name','',False),
		form(0,'text','Amount','amount','',False),
		form(0,'text','NetPrice','netPrice','',False),
		form(0,'text','Properties','properties','',False),
		form(0,'text','Brand','brand','',False),
		form(0,'text','Version','version','',False),
		form(0,'text','Capacity','capacity','',False),
		form(0,'text','Dimension','dimension','',False),
		form(0,'text','Defection','defection','',False),
		form(0,'text','Product Condition','product_condition','',False),
		form(0,'text','Selling Condition','selling_condition','',False),
		form(0,'text','Shipping Condition','shipping_condition','',False),
	]
	context = {
		'forms':forms,
		'categorys':models.Category.objects.all(),
	}
	return context

@common.gen_view('Edit Product Detail','product/editdetail.html',memberOnly=True)
def edit(request,pid):
	product = models.Product.objects.get(id=pid)
	if product.owner != common.getLoginMember(request) :
		raise Exception("Sorry. You're not this product owner.")
	forms = [
		form(0,'text','Name','name',product.name,False),
		form(0,'text','Amount','amount',product.amount,False),
		form(0,'text','NetPrice','netPrice',product.netPrice,False),
		form(0,'text','Properties','properties',product.properties,False),
		form(0,'text','Brand','brand',product.brand,False),
		form(0,'text','Version','version',product.version,False),
		form(0,'text','Capacity','capacity',product.capacity,False),
		form(0,'text','Dimension','dimension',product.dimension,False),
		form(0,'text','Defection','defection',product.defection,False),
		form(0,'text','Product Condition','product_condition',product.product_condition,False),
		form(0,'text','Selling Condition','selling_condition',product.selling_condition,False),
		form(0,'text','Shipping Condition','shipping_condition',product.shipping_condition,False),
	]
	context = {
		'product':product,
		'forms':forms,
		'categorys':models.Category.objects.all(),
	}
	return context

@common.gen_view(postOnly=True,memberOnly=True,redirect=True)
def docreate(request):

	success,result = clean(request, True)
	if not success :
		return result

	return redirect('product_id',pid=result.id)

@common.gen_view(postOnly=True,memberOnly=True,redirect=True)
def doedit(request):

	success,result = clean(request, False)
	if not success :
		return result

	return redirect('product_id',pid=result.id)

def clean(request,isCreate):
	category = request.POST.get('category')
	name = request.POST.get('name')
	amount = request.POST.get('amount')
	netPrice = request.POST.get('netPrice')
	expired = request.POST.get('expired')
	properties = request.POST.get('properties')
	brand = request.POST.get('brand')
	version = request.POST.get('version')
	capacity = request.POST.get('capacity')
	dimension = request.POST.get('dimension')
	defection = request.POST.get('defection')
	product_condition = request.POST.get('product_condition')
	selling_condition = request.POST.get('selling_condition')
	shipping_condition = request.POST.get('shipping_condition')
	picture1 = request.FILES.get('picture1')
	picture2 = request.FILES.get('picture2')
	picture3 = request.FILES.get('picture3')
	picture4 = request.FILES.get('picture4')
	picture5 = request.FILES.get('picture5')

	errorList = {}

	state = request.POST.get('state')
	owner = common.getLoginMember(request)
	try : 
		category=models.Category.objects.get(id=category)
	except : 
		category=models.Category.objects.first()
		errorList['category'] = ['This Category is not in Database']
	try : 
		expired = datetime.datetime.strptime(expired,"%d %b %Y %H:%M")
	except : 
		expired = datetime.datetime.now().replace(year=2000)
		errorList['expired'] = ['This Datetime is not valid format (should be like 23 Dec 2013 23:59)']

	if isCreate :
		product = models.Product(
			state=state,
			owner=owner,
			category=category,
			name=name,
			amount=amount,
			netPrice=netPrice,
			expired=expired,
			properties=properties,
			brand=brand,
			version=version,
			capacity=capacity,
			dimension=dimension,
			defection=defection,
			product_condition=product_condition,
			selling_condition=selling_condition,
			shipping_condition=shipping_condition,
			picture1=picture1,
			picture2=picture2,
			picture3=picture3,
			picture4=picture4,
			picture5=picture5,
			)
	else :
		product = request.POST.get('product')
		product = models.Product.objects.get(id=product)
		if product.owner != owner:
			errorList['owner'] = ['You are not owner of this product']
		if state : product.state = state
		if category : product.category = category
		if name : product.name = name
		if amount : product.amount = amount
		if netPrice : product.netPrice = netPrice
		if expired : product.expired = expired
		if properties : product.properties = properties
		if brand : product.brand = brand
		if version : product.version = version
		if capacity : product.capacity = capacity
		if dimension : product.dimension = dimension
		if defection : product.defection = defection
		if product_condition : product.product_condition = product_condition
		if selling_condition : product.selling_condition = selling_condition
		if shipping_condition : product.shipping_condition = shipping_condition
		if picture1 : product.picture1 = picture1
		if picture2 : product.picture2 = picture2
		if picture3 : product.picture3 = picture3
		if picture4 : product.picture4 = picture4
		if picture5 : product.picture5 = picture5

	try :
		product.full_clean()
	except Exception as e :
		for error in e.args :
			if not error : continue
			for field,exceptions in error.items() :
				errorList[field] = errorList[field] if errorList.get(field) else []
				for exception in exceptions :
					errorList[field].append(unicode(exception)[3:-2])

	context = {}

	if not request.POST.get('isSubmit') :
		if errorList :
			context['errorList'] = errorList
		else :
			context['success'] = True
		return False,common.jsonResponse(context)
	
	if errorList :
		errorListText = []
		for field,error in errorList.items() :
			errorListText.append("%s :: %s"%(field,", ".join(error)))

		context['errorList'] = errorListText
		context['content'] = "Validation Error."
		return False,render(request,'common/invalid.html',context)

	product.save()
	return True,product
