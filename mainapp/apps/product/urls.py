from django.conf.urls import patterns, include, url
from . import editdetail
from . import detail
from . import search
from . import searchlist

urlpatterns = patterns('',
    url(r'detail/', detail.main,name='detail'),
    url(r'editdetai/', editdetail.main,name='editdetail'),
    url(r'search/', search.main,name='search'),
)
