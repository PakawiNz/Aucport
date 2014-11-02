from django.db import models

# Create your models here.
class Member(models.Model) :
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

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
		(STATE_ABANDONED,'abandoned'),
		(STATE_SOLDOUT,'soldout'),
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