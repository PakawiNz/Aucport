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

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin) :
	list_display = ('name',)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin) :
	list_display = ('name','owner','netPrice','state',)

@admin.register(models.Auction)
class AuctionAdmin(admin.ModelAdmin) :
	list_display = ('product','bidder','ceiling','increase','current','isAuto','notify','lastbid',)
	
@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin) :
	list_display = ('timestamp','product','buyer','card','score','comment','critical',)


@admin.register(models.CreditCard)
class CreditCardAdmin(admin.ModelAdmin) :
	list_display = ('owner',)
