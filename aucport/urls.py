from django.conf.urls import patterns, include, url,static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 								'mainapp.apps.views.home',	name='home'),
)

urlpatterns += patterns('mainapp.apps.member',
	url(r'^member/profile/(?P<mid>\d+)/$',		'profile.show',     		name='profile_id'),
	url(r'^member/profile/$', 					'profile.owner',			name='profile'),

	url(r'^member/register/$', 					'register.main',			name='register'),
	url(r'^member/editprofile/$', 				'register.edit',			name='editprofile'),
	url(r'^member/doregister/$', 				'register.register',		name='doregister'),
	url(r'^member/doupdated/$', 				'register.update',			name='doupdated'),
	
	url(r'^member/login/$', 					'authen.login',				name='login'),
	url(r'^member/logout/$', 					'authen.logout',			name='logout'),
	url(r'^member/confirm/$', 					'authen.confirm',			name='confirm'),
)

urlpatterns += patterns('mainapp.apps.product',
	url(r'^product/detail/(?P<pid>\d+)/$', 		'detail.show',				name='product'),
	url(r'^product/create/$', 					'detail.create',			name='c_product'),
	url(r'^product/edit/(?P<pid>\d+)/$', 		'detail.edit',				name='e_product'),
	url(r'^product/do_c_product/$',				'detail.docreate',			name='do_c_product'),
	url(r'^product/do_e_product/$',				'detail.doedit',			name='do_e_product'),

	url(r'^product/search/$', 					'search.main',				name='search'),
)

urlpatterns += patterns('mainapp.apps.trading',
	url(r'^trading/payment/(?P<pid>\d+)/$', 	'payment.main',				name='payment'),
	url(r'^trading/dopayment/$',		 		'payment.payment',			name='dopayment'),

	url(r'^trading/auction/$', 					'auction.main',				name='auction'),
	url(r'^trading/bid/$', 						'auction.bid',				name='bid'),
	url(r'^trading/getupdated/$', 				'auction.getupdated',		name='getupdated'),
	url(r'^trading/watch/(?P<pid>\d+)/$', 		'auction.watch',			name='watch'),
	url(r'^trading/auction_u/$', 				'auction.unwatched_list',	name='auction_u'),

	url(r'^trading/history/$', 					'history.history',			name='transactions'),
	url(r'^trading/feedback/(?P<tid>\d+)/$',	'history.feedback',			name='feedback'),
	url(r'^trading/dofeedback/$', 				'history.dofeedback',		name='dofeedback'),
)

if settings.DEBUG == False :
	urlpatterns += patterns('',
	    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

handler404 = 'mainapp.apps.views.handler404'
handler500 = 'mainapp.apps.views.handler500'