from django.conf.urls import patterns, include, url,static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 								'mainapp.apps.views.home',	name='home'),

) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('mainapp.apps.member',
	url(r'^member/profile/(?P<mid>\d+)/$',	'profile.show',     		),
	url(r'^member/profile/$', 				'profile.owner',			name='profile'),
	url(r'^member/register/$', 				'register.main',			name='register'),
	url(r'^member/editprofile/$', 			'register.edit',			name='editprofile'),
	url(r'^member/doregister/$', 			'register.register',		name='doregister'),
	url(r'^member/doupdated/$', 			'register.update',			name='doupdated'),
	
	url(r'^member/login/$', 				'authen.login',				name='login'),
	url(r'^member/logout/$', 				'authen.logout',			name='logout'),
	url(r'^member/confirm/$', 				'authen.confirm',			name='confirm'),
)

urlpatterns += patterns('mainapp.apps.product',
	url(r'^product/product/(?P<pid>\d+)/$', 'detail.show',				),
	url(r'^product/product/$', 				'detail.dump',				name='product'),
	url(r'^product/c_product/$', 			'detail.create',			name='c_product'),
	url(r'^product/e_product/$', 			'detail.edit',				name='e_product'),
	url(r'^product/do_c_product/$',			'detail.docreate',			name='do_c_product'),
	url(r'^product/do_e_product/$',			'detail.doedit',			name='do_e_product'),
	url(r'^product/search/$', 				'search.form',				name='search'),
	url(r'^product/dosearch/$', 			'search.search',			name='dosearch'),
)

urlpatterns += patterns('mainapp.apps.trading',
	url(r'^trading/auction/$', 				'auction.main',				name='auction'),
	url(r'^trading/payment/$', 				'payment.main',				name='payment'),
	url(r'^trading/bid/$', 					'auction.bid',				name='bid'),
)


handler404 = 'mainapp.utils.error_handler.handler404'
handler500 = 'mainapp.utils.error_handler.handler500'