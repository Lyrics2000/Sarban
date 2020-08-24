from django.contrib import admin
from .models import Category,Products,PostImage,MoreProductQuantirty

# Register your models here.
class MoreProductQuantityInline(admin.StackedInline):
        model = MoreProductQuantirty
class PostImageAdmin(admin.StackedInline):
        model = PostImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug']
    class Meta:
        model = Category
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug']
    inlines = [MoreProductQuantityInline,PostImageAdmin]
    class Meta:
        model = Products

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(PostImage)
admin.site.register(MoreProductQuantirty)
