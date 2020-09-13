from django.contrib import admin
from .models import Address,DeliveryTime

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'addresstype','address_line1','address_line2','city','name','email','phone']
    class Meta:
        model = Address

class DeiveryTimedmin(admin.ModelAdmin):
    list_display = ['__str__' , 'date']
    class Meta:
        model = DeliveryTime
admin.site.register(Address,AddressAdmin)
admin.site.register(DeliveryTime,DeiveryTimedmin)
