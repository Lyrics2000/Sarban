from django.db import models
import random
import os
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from .utils import unique_slug_generator,category_unique_slug_generator
# Create your models here.

CATEGORY_STATUS = (
    ('Ac', 'Active'),
    ('In', 'InActive'),
    
)

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )

def upload_image_path2(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "categories/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.FileField(upload_to = upload_image_path2 ,null=True,blank=False)
    category_description = models.TextField()
    slug = models.SlugField(blank=True,unique=True)
    

    def __str__(self):
        return self.category_name



class Products(models.Model):
    product_title = models.CharField(max_length=100)
    product_overview = models.CharField(max_length=100)
    product_full_description = models.TextField()
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_quantity_in_kgs = models.DecimalField(max_digits=5, decimal_places=2)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_discount_price = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    product_status = models.CharField(choices=CATEGORY_STATUS,max_length=2)
    product_Image_Field = models.ImageField(upload_to=upload_image_path,null=True,blank=False)
    featured_product = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now, editable=False)
    slug = models.SlugField(blank=True,unique=True)
    def __str__(self):
        return self.product_title
    
    def get_percentage_off(self):
        newmoriginal = self.product_price - self.product_discount_price
        percentage = (newmoriginal/self.product_price) * 100
        return int(percentage)
    def new_products(self):
        original_date = self.created_date
        subtracteddate = original_date - now()

        return subtracteddate
    
    def return_two_weeks(self):
        two_weeks = datetime.timedelta(hours=336)
        return two_weeks
    def get_absolute_url(self):
        return reverse("products:product", kwargs={
            'slug': self.slug
        })

    def moreq(self):
        qs = MoreProductQuantirty.objects.all()
        return qs
  
    



def product_presave_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_presave_reciver,sender = Products)

def category_presave_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = category_unique_slug_generator(instance)


pre_save.connect(category_presave_reciver,sender = Category)

class PostImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    more_images = models.ImageField(upload_to=upload_image_path,null=True,blank=True)

    def __str__(self):
        return self.product.product_title

class MoreProductQuantirty(models.Model):
    product_more = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    more_product_quantity = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.product_more.product_title
        





    
