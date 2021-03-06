from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

     url(r'^$', 'products.views.home', name='home'),
     url(r'^products/$', 'products.views.all', name='products'),
     url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
     url(r'^s/$', 'products.views.search', name='search'),
     url(r'^cart/$', 'carts.views.view', name='cart'),
     url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
     url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),

    url(r'^admin/', include(admin.site.urls)),
) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

