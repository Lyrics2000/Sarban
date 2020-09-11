from django.shortcuts import render,redirect
from billing.models import BillingProfile
from accounts.forms import GuestForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm,DeliveryTimeAddress
from addresses.models import Address,DeliveryTime
from orders.models import Order
from products.models import Products,Category,Banners
from .models import Cart,CartQuantity
from orders.models import Order
from decimal import Decimal
from addresses.utils import API_KEY,gmap_key,distancePriceCalculator,newport_ri
from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math



# Create your views here.



def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    cart_items = cart_obj.products.count()
    allcategory = Category.objects.all()
    
    context = {
        'cart' : cart_obj,
        'cart_items' : cart_items,
        'categories' : allcategory,
    } 
    return render(request,'carts/home.html',context)



def cart_update(request):
    product_id = request.POST.get("product_id")
    quantity = request.POST.get("quantity")

    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        print("Product object is " , product_obj)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        
        if product_obj in cart_obj.products.all():
            print("The cart object is" ,  cart_obj)
            cart_obj.products.remove(product_obj)
            instance = CartQuantity.objects.filter(product=str(product_obj))
            instance.delete()
        else:
            cart_obj.products.add(product_obj)
            cart_quantity = CartQuantity.objects.create(cart=cart_obj)
            cart_quantity.product = str(product_obj)
            if quantity:
                cart_quantity.quantity = quantity
                cart_quantity.save()
            else:
                cart_quantity.quantity = 1
                cart_quantity.save()
                    
        
        all_products = CartQuantity.objects.all()
        cart_total = 0
        product_toatal = 0
        for x in all_products:
            if x.cart == cart_obj:
                mvbb = Products.objects.get(product_title__iexact = str(x.product))
                if mvbb:
                    if mvbb.product_discount_price:
                        msv = mvbb.product_discount_price * x.quantity
                        product_toatal += msv
                    else:
        
                        msv = mvbb.product_price * x.quantity
                        product_toatal += msv

    
        cart_id = request.session.get("cart_id")
        mnupdat  = Cart.objects.get(id = cart_id)
        mnupdat.subtotal = product_toatal
        mnupdat.total = product_toatal
        mnupdat.save()    
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("carts:checkout")

def cart_remove(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            del  request.session['cart_id']
            
        
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("/")

def cart_remove_wishlist(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.remove(product_obj)
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("cart:cart_home")

def cart_remove_checkout(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.remove(product_obj)
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("cart:checkout")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:cart_home")  
    guest_form = GuestForm()
    address_form = AddressForm()
    delivery_form  = DeliveryTimeAddress()
    shipping_address_id = request.session.get("delivery_address_id" , None)
    delivery_time_id  = request.session.get('delivery_time' , None)
    billing_profile, billing_profile_created  = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj,order_obj_created = Order.objects.new_or_get(billing_profile,cart_obj)
        if shipping_address_id:
            order_obj.delivery_address = Address.objects.get(id=shipping_address_id)
            #calculating shipping address
            shipping_addresses = Address.objects.get(id=shipping_address_id)
            print(shipping_addresses.address_line1)
            geolocator = Nominatim(user_agent="carts")
            location = gmap_key.geocode(shipping_addresses.address_line1)
            lat = location[0]["geometry"]["location"]["lat"]
            lon = location[0]["geometry"]["location"]["lng"]
            print("location" ,  location)
            #customer location
            cleveland_oh = (lat, lon)
            
            #calculate the distace price
            distancec  = geodesic(newport_ri, cleveland_oh).km
            price = distancePriceCalculator(distance=distancec)
            #set shipping price to delivery price calculated
            order_obj.shipping_total = price
            new_total = math.fsum([cart_obj.total, price])
            formatted_total = format(new_total,'2')
            order_obj.total = new_total


            if delivery_time_id:
                order_obj.delivery_time = DeliveryTime.objects.get(id=delivery_time_id)



    
           
        

        if  shipping_address_id:
            order_obj.save()
           
    cart_items  = cart_obj.products.count()
    allcategory = Category.objects.all()
    allbanners = Banners.objects.all()
    cartqty = CartQuantity.objects.all()
    google_api = API_KEY
   
    
    request.session['object'] = str(order_obj)
    request.session['cart'] = str(cart_obj)
    request.session['cart_items'] = cart_items
 
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "address_form" : address_form,
         "address_qs" : address_qs,
        "guest_form": guest_form,
        "cart_items" :  cart_items,
        "cart_obj" : cart_obj,
        "cart" : cart_obj,
        'categories' : allcategory,
        'delivery_form' : delivery_form,
        'allbanners'    : allbanners,
        'cartqty'    : cartqty,
        'google_api' : google_api
    }
    return render(request, "carts/checkout.html", context)