
from django.contrib import admin
from django.urls import path,include
from .views import (ItemDetailView,
FeaturedProducts,
NewProduct,
Index,
ItemDetailViewCategory)

app_name = 'products'


urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('category/<slug>/', ItemDetailViewCategory.as_view(), name='category'),
    path('newproducts/', NewProduct.as_view(), name='newproducts'),
    path('featuredproducts/', FeaturedProducts.as_view(), name='featured'),
    
]
