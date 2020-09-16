from django.contrib import admin
from .models import Contacts
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'full_name' , 'email_address','subject','message',
    ]
#     inlines = [MoreProductQuantityInline,PostImageAdmin]
    class Meta:
        model = Contacts

admin.site.register(Contacts,ContactAdmin)

