from django.db import models
import hashlib

# Create your models here.

class Country(models.Model) :
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class Timezone(models.Model) :
	name = models.CharField(max_length=80)
	offset = models.IntegerField()
	def __unicode__(self):
		return self.name

class Member(models.Model) :
	def content_file_name(instance, filename):
		filename = hashlib.sha224(instance.email).hexdigest()
		return '/'.join(['profilepic', filename + '.jpg'])

	email = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	displayname = models.CharField(max_length=50,unique=True)
	birthdate = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	country = models.ForeignKey(Country)
	timezone = models.ForeignKey(Timezone)
	confirmation = models.CharField(max_length=100)
	isConfirmed = models.BooleanField(default=False)
	picture = models.FileField(upload_to=content_file_name,null=True)

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

class Auction(models.Model) :
	product = models.OneToOneField(Product)

class Transaction(models.Model) :
	product = models.ForeignKey(Product)
	buyer = models.ForeignKey(Member)

class Feedback(models.Model) :
	transaction = models.ForeignKey(Transaction)

class Comment(models.Model) :
	product = models.ForeignKey(Product)

class CreditCard(models.Model) :
	owner = models.ForeignKey(Member)
