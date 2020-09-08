from django.db import models
from django.conf import settings
from products.models import Products
from django.db.models.signals import pre_save,m2m_changed
User = settings.AUTH_USER_MODEL
from decimal import Decimal
# Create your models here.
class CartManager(models.Manager):
  
    def new_or_get(self,request):
        cart_id  = request.session.get("cart_id" , None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user =  request.user
                cart_obj.save()
        else:
            cart_obj = self.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj,new_obj

    def new(self,user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    products = models.ManyToManyField(Products,blank=True)
    subtotal = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updates = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)
    
    def price(self):
        if self.products.product_discount_price:
            return Decimal(self.products.product_discount_price)
        else:
            return Decimal(self.products.product_price)


# def m2m_save_receiver(sender,instance,action,*args,**kwargs):
#     if action == 'post_remove' or action == 'post_add' or action == 'post_clear':
#         products = instance.products.all()
#         total = 0
#         for x in products:
#             if x.product_discount_price:
#                 total +=x.product_discount_price
#             else:
#                 total +=x.product_price
#         if instance.subtotal != total:
#             instance.subtotal = total
#             instance.save()
        
# m2m_changed.connect(m2m_save_receiver,sender=Cart.products.through)


# def pre_save_cart_reciever(sender,instance,*args,**kwargs):
#     if instance.subtotal > 0:
#         instance.total = instance.subtotal 
#     else:
#         instance.total = 0.00


# pre_save.connect(pre_save_cart_reciever,sender = Cart)

class CartQuantity(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return str(self.cart)
   
    
    
