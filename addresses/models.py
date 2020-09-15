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
    address_line2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    estate_decsription = models.CharField(max_length=120,blank=True,null=True)


    def __str__(self):
        return str(self.billing_profile)



class DeliveryTime(models.Model):
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True,null=True)
    

    def __str__(self):
        return str(self.date)
    
    

