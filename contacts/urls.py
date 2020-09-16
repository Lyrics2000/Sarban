

from django.urls import path
from .views import index

app_name = 'contacts'


urlpatterns = [
    path('',index,name= 'contacts_index'),
     
    
    
]
