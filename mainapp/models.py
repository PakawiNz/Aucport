from django.db import models

from utils import fields,validator as V
import datetime

def get_one(model,**kwargs) :
 	alist = model.objects.filter(**kwargs)
 	if alist : return alist[0]
	else : return None

# Create your models here.
class Country(models.Model) :
	name = fields.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Timezone(models.Model) :
	name = fields.CharField(max_length=80)
	offset = models.IntegerField()
	def __unicode__(self):
		return self.name

class Member(models.Model) :
	email = models.EmailField(unique=True)
	password = fields.CharField(min_length=8, max_length=50)
	firstname = fields.AlphaNumericField(min_length=1, max_length=50)
	lastname = fields.AlphaNumericField(min_length=1, max_length=50)
	displayname = fields.RegexField(regex=r'[A-z](\w ?)*\w$', max_length=50,unique=True)
	birthdate = fields.BirthdateField(minimum_age=8)
	address = fields.RegexField(regex=r'\w+[\w ,./]*$',max_length=50)
	phone = fields.RegexField(regex=r'[0-9]{5,}$',max_length=50)
	country = models.ForeignKey(Country)
	timezone = models.ForeignKey(Timezone)
	confirmation = fields.CharField(max_length=100)
	isConfirmed = models.BooleanField(default=False)
	picture = models.ImageField(upload_to=fields.member_file_name,null=True,blank=True)

	def __unicode__(self):
		return self.email

class Category(models.Model) :
	name = fields.CharField(max_length=80)
	parent = models.ForeignKey('self',null=True,blank=True,related_name="children")

	def __unicode__(self):
		return self.name

class Product(models.Model) :

	STATE_PENDING = 1
	STATE_SELLING = 2
	STATE_AUCTION = 3
	STATE_BILLING = 4
	STATE_ABANDONED = 5
	STATE_SOLDOUT = 6
	__state = (
		(STATE_PENDING,'pending'),
		(STATE_SELLING,'selling'),
		(STATE_AUCTION,'auction'),
		(STATE_BILLING,'billing'),
		(STATE_SOLDOUT,'soldout'),
		(STATE_ABANDONED,'abandoned'),
	)

	state = models.IntegerField(choices=__state)
	category = models.ForeignKey(Category)
	owner = models.ForeignKey(Member)
	
	name = models.CharField(max_length=50)
	amount = models.CharField(max_length=50)
	
	netPrice = models.FloatField()
	expired = models.DateTimeField()
	picture1 = models.ImageField(upload_to=fields.product_file_name,null=True,blank=True)
	picture2 = models.ImageField(upload_to=fields.product_file_name,null=True,blank=True)
	picture3 = models.ImageField(upload_to=fields.product_file_name,null=True,blank=True)
	picture4 = models.ImageField(upload_to=fields.product_file_name,null=True,blank=True)
	picture5 = models.ImageField(upload_to=fields.product_file_name,null=True,blank=True)

	properties = models.TextField(null=True,blank=True)
	brand = models.CharField(max_length=50,null=True,blank=True)
	version = models.CharField(max_length=50,null=True,blank=True)
	capacity = models.CharField(max_length=50,null=True,blank=True)
	dimension = models.CharField(max_length=50,null=True,blank=True)
	defection = models.CharField(max_length=50,null=True,blank=True)
	product_condition = models.TextField(null=True,blank=True)
	selling_condition = models.TextField(null=True,blank=True)
	shipping_condition = models.TextField(null=True,blank=True)

	highest_auction = models.OneToOneField('Auction',related_name="highest_auction",null=True,blank=True)

	def __unicode__(self):
		return self.name


class Auction(models.Model) :
	product = models.ForeignKey(Product)
	bidder = models.ForeignKey(Member)
	ceiling = models.FloatField(default=0)
	increase = models.FloatField(default=0)
	current = models.FloatField()
	isAuto = models.BooleanField(default=False)
	notify = models.BooleanField(default=False)
	lastbid = models.DateTimeField()

	def __unicode__(self):
		return self.bidder.displayname

				
class Transaction(models.Model) :
	product = models.ForeignKey(Product)
	buyer = models.ForeignKey(Member)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.product.name

class Feedback(models.Model) :
	transaction = models.ForeignKey(Transaction)
	isReport = models.BooleanField(default=False)
	score = models.IntegerField()

class CreditCard(models.Model) :
	owner = models.ForeignKey(Member)

