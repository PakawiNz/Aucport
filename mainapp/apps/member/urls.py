from django.conf.urls import patterns, include, url
from . import register

urlpatterns = patterns('',
    url(r'register/', register.main,name='register'),
)
