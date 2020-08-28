from django.db import models
from billing.models import BillingProfile

# Create your models here.
ADDRESS_TYPES = (
    ('delivery', 'Delivery'),
   
)
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    addresstype = models.CharField(max_length=120,choices=ADDRESS_TYPES)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, default = "Kangemi")
    city = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)
