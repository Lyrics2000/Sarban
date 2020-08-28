
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from addresses.views import checkout_address_create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('checkout/address/create',checkout_address_create_view, name='checkout_address_create_view'),
    path('search/',include('search.urls', namespace='search')),
     path('carts/',include('carts.urls', namespace='cart')),
     path('account/' ,include('accounts.urls' , namespace = 'account'))
]

if settings.DEBUG:
    urlpatterns  =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns  =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)