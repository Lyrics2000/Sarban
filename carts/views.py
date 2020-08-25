from django.shortcuts import render,redirect
from orders.models import Order
from products.models import Products
from .models import Cart
# Create your views here.



def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    cart_items = cart_obj.products.count()
    context = {
        'cart' : cart_obj,
        'cart_items' : cart_items,
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
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("carts:cart_home")



def checkout_home(request):
    cart_obj,cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("carts:cart_home")
    else:
        order_obj,new_order_obj = Order.objects.get_or_create(cart=cart_obj)
        context = {
            'object' : order_obj
        }
    return render(request,'carts/checkout.html',context)







