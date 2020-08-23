
from django.contrib import admin
from django.urls import path,include
from .views import index,ItemDetailView,featuredproducts,newproducts

app_name = 'products'


urlpatterns = [
    path('',index,name='index'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('newproducts/', newproducts, name='newproducts'),
    path('featuredproducts/', featuredproducts, name='featured'),
    
]
