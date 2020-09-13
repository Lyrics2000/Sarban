from django.contrib import admin
from .models import Cart,CartQuantity
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'user','subtotal','total','updates','timestamp']
    class Meta:
        model = Cart
admin.site.register(Cart,CartAdmin)
admin.site.register(CartQuantity)
