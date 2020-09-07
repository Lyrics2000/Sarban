
from django.contrib import admin
from django.urls import path,include
from .views import (Index,
lipa_na_mpesa_online,
register_urls,
confirmation,
validation,
call_back,
cash_on_delivery,
cash_on_delivery_success,
simulate_mpesa
)

app_name = 'mpesa'


urlpatterns = [
    path('',Index,name='mpesaindex'),
    path('online/lipa', lipa_na_mpesa_online, name='lipa_na_mpesa'),

     # register, confirmation, validation and callback urls
    path('c2b/register', register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', confirmation, name="confirmation"),
    path('c2b/validation', validation, name="validation"),
    path('c2b/callback', call_back, name="call_back"),
    path('cash_on_delivery',cash_on_delivery, name="cash_on_delivery"),
    path('cash_on_delivery/success',cash_on_delivery_success, name="cash_on_delivery_success"),

    #simulate mpesa
    path('c2b/mpesa', simulate_mpesa, name="simulate_mpesa"),
    
    
]
