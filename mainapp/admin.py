from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin) :
	list_display = ('name',)

@admin.register(models.Timezone)
class TimezoneAdmin(admin.ModelAdmin) :
	list_display = ('name','offset',)

@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin) :
	list_display = ('email','firstname','lastname','displayname','birthdate','address','country','timezone','isConfirmed')

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin) :
	list_display = ('owner','netPrice','state',)

@admin.register(models.Auction)
class AuctionAdmin(admin.ModelAdmin) :
	list_display = ('product',)

@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin) :
	list_display = ('product','buyer',)

@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin) :
	list_display = ('transaction',)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin) :
	list_display = ('product',)

@admin.register(models.CreditCard)
class CreditCardAdmin(admin.ModelAdmin) :
	list_display = ('owner',)
