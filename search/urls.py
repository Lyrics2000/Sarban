
from django.contrib import admin
from django.urls import path,include
from products.views import NewProduct

app_name = 'products'


urlpatterns = [
   
    path('', NewProduct.as_view(), name='newproducts'),
    
    
]
