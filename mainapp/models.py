from django.db import models

from utils import fields,validator as V
import datetime

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
	picture = models.ImageField(upload_to=fields.member_file_name,null=True)

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
	owner = models.ForeignKey(Member)
	netPrice = models.FloatField()
	state = models.IntegerField(choices=__state)
	expired = models.DateTimeField()
	picture1 = models.ImageField(upload_to=fields.product_file_name,null=True)
	picture2 = models.ImageField(upload_to=fields.product_file_name,null=True)
	picture3 = models.ImageField(upload_to=fields.product_file_name,null=True)
	picture4 = models.ImageField(upload_to=fields.product_file_name,null=True)
	picture5 = models.ImageField(upload_to=fields.product_file_name,null=True)

	# product_name
	# product_brand
	# product_version
	# product_capacity
	# product_properties
	# product_dimension
	# product_amount
	# product_defection
	# product_condition

	# selling_condition
	# shipping_condition
	# increasing_price

class Auction(models.Model) :
	product = models.ForeignKey(Product)
	bidder = models.ForeignKey(Member)
	ceiling = models.FloatField(default=0)
	increase = models.FloatField(default=0)
	current = models.FloatField()
	isAuto = models.BooleanField(default=False)
	notify = models.BooleanField(default=False)
	lastbid = models.DateTimeField()

	def bid(self,amount=0) :
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
				

class Transaction(models.Model) :
	product = models.ForeignKey(Product)
	buyer = models.ForeignKey(Member)
	timestamp = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model) :
	transaction = models.ForeignKey(Transaction)
	isReport = models.BooleanField(default=False)
	score = models.IntegerField()

class CreditCard(models.Model) :
	owner = models.ForeignKey(Member)
