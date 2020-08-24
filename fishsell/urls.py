
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('search/',include('search.urls', namespace='search')),
     path('carts/',include('carts.urls', namespace='cart')),
]

if settings.DEBUG:
    urlpatterns  =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns  =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)