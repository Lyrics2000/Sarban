from django.contrib import admin
from .models import Address,DeliveryTime

# Register your models here.
admin.site.register(Address)
admin.site.register(DeliveryTime)
