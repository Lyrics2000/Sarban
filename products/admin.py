from django.contrib import admin
from .models import Category,Products,Banners

# Register your models here.
# class MoreProductQuantityInline(admin.StackedInline):
#         model = MoreProductQuantirty
# class PostImageAdmin(admin.StackedInline):
#         model = PostImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug']
    class Meta:
        model = Category
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug' , 'product_category','product_quantity_in_kgs','product_price',
    'product_discount_price','featured_product']
#     inlines = [MoreProductQuantityInline,PostImageAdmin]
    class Meta:
        model = Products

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products,ProductAdmin)

admin.site.register(Banners)
