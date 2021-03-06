from django.shortcuts import render,redirect
from.forms import AddressForm,DeliveryTimeAddress
from billing.models import BillingProfile
from django.utils.http import is_safe_url
from .models import Address


# Create your views here.
def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {
        'form' : form
    }
    next = request.GET.get('next')
    next_post = request.GET.get('next')
    redirect_path = next or next_post or None
    if form.is_valid:
        
        instance = form.save(commit=False)
        billing_profile,billing_profile_created = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            
            instance.billing_profile = billing_profile
            instance.addresstype = "delivery"
            instance.save()
            request.session["delivery" + "_address_id"] = instance.id
            #print(billing_profile)
            
        else:
            redirect("cart:checkout")
        if is_safe_url(redirect_path,request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("cart:checkout")
    return redirect("carts:checkout")


def deliver_time(request):
    form = DeliveryTimeAddress(request.POST or None)
    if form.is_valid:
        instance = form.save(commit=False)
        address_id = request.session.get("delivery_address_id")
        all_address_with_specific_id = Address.objects.get(id = address_id)
        instance.address = all_address_with_specific_id
        instance.save()
        request.session["delivery_time"] = instance.id
        return redirect("cart:checkout")
    return redirect("carts:checkout")





