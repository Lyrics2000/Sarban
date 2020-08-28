
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import signin,signup,guest_register_view

app_name = 'accounts'


urlpatterns = [
    path('',signin,name= 'signin'),
     path('signup',signup,name= 'signup'),
     path('signup/guest/',guest_register_view,name= 'guest_register'),
     path('logout',LogoutView.as_view() , name="logout"),
    
    
]
