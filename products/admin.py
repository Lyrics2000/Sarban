from django.contrib import admin
from .models import Category,Products

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug']
    class Meta:
        model = Category
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug']
    class Meta:
        model = Products

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products,ProductAdmin)