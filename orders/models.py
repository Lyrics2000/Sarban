import math
from django.db import models
from django.db.models.signals import pre_save,post_save
from addresses.models import Address
from billing.models import BillingProfile
from carts.models import Cart
from fishsell.utils import unique_order_id_generator
import requests

ORDER_STATUS_CHOICES = (
    ('created' , 'Created'),
    ('paid' , 'Paid'),
    ('shipped' , 'Shipped'),
    
)
# Create your models here.
class OrderManager(models.Manager):
    def new_or_get(self,billing_profile,cart_obj):
        created = False
        qs = self.get_queryset().filter(billing_profile=billing_profile, cart=cart_obj, active=True, status = 'created')
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(billing_profile=billing_profile, cart=cart_obj)
            created = True
        return obj,created
    def shipping__totals(self):
       
        values = """
  {
    "command": "request",
    "data": {
      "api_key": "wkcgYXYcQIGUMpDbSRqB",
      "api_username": "handlings254",
      "vendor_type": 1,
      "rider_phone": "0728561783",
      "from": {
        "from_name": "Green House",
        "from_lat": -1.300577,
        "from_long": 36.78183,
        "from_description": ""
      },
      "to": {
        "to_name": "KICC",
        "to_lat": -1.28869,
        "to_long": 36.823363,
        "to_description": ""
      },
      "recepient": {
          
        "recepient_name": "Sender Name",
        "recepient_phone": "0709779779",
        "recepient_email": "sendyer@gmail.com",
        "recepient_notes": "recepient specific Notes",
        "recepient_notify": false
      },
      "sender": {
        "sender_name": "Sendyer Name",
        "sender_phone": "0709 779 779",
        "sender_email": "sendyer@gmail.com",
        "sender_notes": "Sender specific notes",
        "sender_notify": false
      },
      "delivery_details": {
        "pick_up_date": "2016-04-20 12:12:12",
        "collect_payment": {
          "status": false,
          "pay_method": 0,
          "amount": 10
        },
        "carrier_type": 2,
        "return": false,
        "note": " Sample note",
        "note_status": true,
        "request_type": "delivery",
        "order_type": "ondemand_delivery",
        "ecommerce_order": false,
        "express": false,
        "skew": 1,
        "package_size": [
          {
            "weight": 20,
            "height": 10,
            "width": 200,
            "length": 30,
            "item_name": "laptop"
          }
        ]
      }
    },
    "request_token_id": "request_token_id"
  }
"""

        headers = {
        'Content-Type': 'application/json'
            }
        request = requests.post('https://apitest.sendyit.com/v1/#request', data=values, headers=headers)
        return request.json()
    
    


class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE,null=True,blank=True)
    order_id = models.CharField(max_length=120,blank=True)
    delivery_address = models.ForeignKey(Address,related_name="delivery_address",on_delete=models.CASCADE,null=True,blank=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(max_length=120,default='created',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=00.00,max_digits=100,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.order_id
    objects = OrderManager()
   
    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        # You can calculate tax here
        # shipping totals can also be calculated here
        new_total = math.fsum([cart_total , shipping_total])
        formatted_total = format(new_total,'2')
        self.total = formatted_total
        self.save()
        return new_total
    #checking theat the model is done
    def check_done(self):
        billing_profile = self.billing_profile
        shipping_address  = self.shipping_address
        billing_address = self.billing_address
        total = self.total
        if billing_profile and shipping_address and billing_address and total > 0:
            return True
        return False
    def mark_paid(self):
        if self.check_done():
            self.status = 'paid'
            self.save()
        return self.status


def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)




pre_save.connect(pre_save_create_order_id,sender = Order)

def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id = cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total,sender = Cart)

def post_save_order(sender,instance,created,*args,**kwargs):
    print("running...")
    if created:
        print("updating first...")
        instance.update_total()

post_save.connect(post_save_order,sender = Order)






