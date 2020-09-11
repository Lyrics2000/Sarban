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


    def __str__(self):
        return str(self.billing_profile)


DELIVER_ADDRESS_TIME = (
    
    ('a', '8:00 AM - 10:00 AM'),
     ('b', '10:00 AM - 12:00 PM'),
      ('c', '12:00 PM - 2:00 PM'),
       ('d', '2:00 PM - 4:00 PM'),
        ('e', '4:00 PM - 6:00 PM'),
   
)
class DeliveryTime(models.Model):
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    date = models.DateField(blank=True,null=True)
    time = models.CharField(max_length=150,choices=DELIVER_ADDRESS_TIME,null=True,blank=True)

    def __str__(self):
        return str(self.address)
    
    def gettime(self):
        return str(self.time)

