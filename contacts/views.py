from django.shortcuts import render,redirect
from carts.models import Cart
from .forms import ContactsForm
from .models import Contacts
from products.models import Products,Category,Banners

# Create your views here.

def index(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    cart_items = cart_obj.products.count()
    allcategory = Category.objects.all()
    form = ContactsForm()
    if request.POST:
        if form.is_valid:
            instance  = ContactsForm(request.POST, None)
            instance.save()
            return redirect("products:index")
        
    
    context = {
        'cart' : cart_obj,
        'cart_items' : cart_items,
        'categories' : allcategory,
        'form' : form
    } 
    return render(request,'contacts.html', context)
