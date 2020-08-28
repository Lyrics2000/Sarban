from django.shortcuts import render,redirect
from billing.models import BillingProfile
from accounts.forms import GuestForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
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

    return redirect("carts:checkout")

def cart_remove(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.remove(product_obj)
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("/")



def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:cart_home")  
    
    
    
    guest_form = GuestForm()
    address_form = AddressForm()
    shipping_address_id = request.session.get("delivery_address_id" , None)
    billing_profile, billing_profile_created  = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        address_qs = Address.objects.filter(billing_profile=billing_profile)
        # shipping_address_qs = address_qs.filter(addresstype = 'shipping')
        # billing_address_qs = address_qs.filter(addresstype = 'billing')
        order_obj,order_obj_created = Order.objects.new_or_get(billing_profile,cart_obj)
        if shipping_address_id:
            order_obj.delivery_address = Address.objects.get(id=shipping_address_id)
            del request.session["delivery_address_id"]
        
        if  shipping_address_id:
            order_obj.save()

    if request.method == "POST":
        #to do: do some check to see that the order is done
        #update order object to being paid 
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            del request.session['cart_id'] 
            return redirect("/cart/success")
    cart_items  = cart_obj.products.count()
 
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "address_form" : address_form,
         "address_qs" : address_qs,
        "guest_form": guest_form,
        "cart_items" :  cart_items,
        "cart_obj" : cart_obj
    }
    return render(request, "carts/checkout.html", context)