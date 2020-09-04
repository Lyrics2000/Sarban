
from django.contrib import admin
from django.urls import path,include
from .views import (Index,
lipa_na_mpesa_online,
register_urls,
confirmation,
validation,
call_back
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
    
    
]
