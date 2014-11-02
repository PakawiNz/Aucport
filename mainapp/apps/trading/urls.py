from django.conf.urls import patterns, include, url
from . import auction
from . import payment

urlpatterns = patterns('',
    url(r'auction/', auction.main,name='auction'),
    url(r'payment/', payment.main,name='payment'),
)
