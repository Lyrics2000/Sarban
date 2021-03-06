from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'delivery_address','delivery_time','cart','status','shipping_total','total','active','cash_at_hand','change_expected']
    class Meta:
        model = Order
admin.site.register(Order,OrderAdmin)
