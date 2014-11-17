from django.conf.urls import patterns, include, url
from . import register
from . import profile
from . import editprofile
from . import authen

urlpatterns = patterns('',
    url(r'editprofile/', editprofile.main,name='editprofile'),
    url(r'profile/', profile.main,name='profile'),
    url(r'register/', register.main,name='register'),
    url(r'login/', authen.login,name='login'),
    url(r'logout/', authen.logout,name='logout'),
    url(r'confirm/', authen.confirm,name='confirm'),
)
