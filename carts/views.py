from django.shortcuts import render,redirect
from products.models import Products
from .models import Cart
# Create your views here.



def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart' : cart_obj
    } 
    return render(request,'carts/home.html',context)



def cart_update(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)

    return redirect("carts:cart_home")



