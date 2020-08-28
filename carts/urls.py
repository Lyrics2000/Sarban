

from django.urls import path
from .views import cart_home,cart_update,checkout_home,cart_remove,cart_remove_wishlist,cart_remove_checkout

app_name = 'carts'


urlpatterns = [
    path('',cart_home,name= 'cart_home'),
     path('checkout',checkout_home,name= 'checkout'),
    path('update',cart_update,name= 'cart_update'),
    path('remove',cart_remove,name= 'cart_remove_product'),
    path('remove_wishlist',cart_remove_wishlist,name= 'cart_remove_product_wishlist'),
    path('remove_checkout',cart_remove_checkout,name= 'cart_remove_checkout'),
    
    
]
