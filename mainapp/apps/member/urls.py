from django.conf.urls import patterns, include, url
from . import register
from . import profile
from . import editprofile

urlpatterns = patterns('',
    url(r'editprofile/', editprofile.main,name='editprofile'),
    url(r'profile/', profile.main,name='profile'),
    url(r'register/', register.main,name='register'),
)
