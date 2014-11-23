from django.conf.urls import patterns, include, url,static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),

) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('mainapp.apps.member',
	url(r'^member/profile/(?P<mid>\d+)/$',	'profile.show',     		name='profile_of'),
	url(r'^member/profile/$', 				'profile.owner',			name='profile'),
	url(r'^member/editprofile/$', 			'profile.edit',				name='editprofile'),
	url(r'^member/register/$', 				'register.main',			name='register'),
	url(r'^member/doregister/$', 			'register.register',		name='doregister'),
	
	url(r'^member/login/$', 				'authen.login',				name='login'),
	url(r'^member/logout/$', 				'authen.logout',			name='logout'),
	url(r'^member/confirm/$', 				'authen.confirm',			name='confirm'),
)

urlpatterns += patterns('mainapp.apps.product',
	url(r'^product/detail/$', 				'detail.show',				name='detail'),
	url(r'^product/editdetail/$', 			'detail.edit',				name='editdetail'),
	url(r'^product/search/$', 				'search.form',				name='search'),
	url(r'^product/dosearch/$', 			'search.search',			name='dosearch'),
)

urlpatterns += patterns('mainapp.apps.trading',
	url(r'^trading/auction/$', 				'auction.main',				name='auction'),
	url(r'^trading/payment/$', 				'payment.main',				name='payment'),
	url(r'^trading/bid/$', 					'auction.bid',				name='bid'),
)
