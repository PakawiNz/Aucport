from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aucport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^member/', include('mainapp.apps.member.urls')),
    url(r'^product/', include('mainapp.apps.product.urls')),
    url(r'^trading/', include('mainapp.apps.trading.urls')),
)
