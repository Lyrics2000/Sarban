from django.shortcuts import render,redirect
from carts.models import Cart
from billing.models import BillingProfile
from addresses.models import Address,DeliveryTime
from orders.models import Order
from products.models import Category

#Email imports
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

#####################
# Create your views here.
from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment

def Index(request):
    order_id = request.session.get('object' ,  None)
    cart_id = request.session.get('cart' , None)
    cart_items = request.session.get('cart_items' , None)
    allcategory = Category.objects.all()
    order_obj = Order.objects.get(order_id__iexact =order_id)
    cart_obj = Cart.objects.get(id__iexact = cart_id)
    context = {
        "object": order_obj,
        "cart_items" :  cart_items,
        "cart_obj" : cart_obj,
        "cart" : cart_obj,
        "delivery_method" : "continue with Mpesa"
       
    }
    return render(request, "mpesa.html", context)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254704157038,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254704157038,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Lyrics Dribbler",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    mpesa_respone = json.loads(response.text)
    return HttpResponse(mpesa_respone)




@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Cancelled",
               "ConfirmationURL": "http://sleepy-savannah-28536.herokuapp.com/api/v1/c2b/confirmation",
               "ValidationURL": "http://sleepy-savannah-28536.herokuapp.com/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)

    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):

    context = {
        "ResultCode": 0,
        "Amount" :  2,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],

    )
    payment.save()

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse(dict(context))



def cash_on_delivery(request):
    order_id = request.session.get('object' ,  None)
    cart_id = request.session.get('cart' , None)
    cart_items = request.session.get('cart_items' , None)
    allcategory = Category.objects.all()
    order_obj = Order.objects.get(order_id__iexact =order_id)
    cart_obj = Cart.objects.get(id__iexact = cart_id)

    if  request.method == "POST" :
        #to do: do some check to see that the order is done
        #update order object to being paid 
        # href="{% url 'mpesa:lipa_na_mpesa' %}"
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_cash_on_delivery()
            del request.session['cart_id'] 
            return redirect("mpesa:cash_on_delivery_success")

    context = {
        "object": order_obj,
        "cart_items" :  cart_items,
        "cart_obj" : cart_obj,
        "cart" : cart_obj,
        "delivery_method" : "continue with cash on delivery",
        "form_cash" : "cash"
    }
    return render(request, "cash.html", context)


def cash_on_delivery_success(request):
    delivery_time_id  = request.session.get('delivery_time' , None)
    
    order_id = request.session.get('object' ,  None)
    cart_id = request.session.get('cart' , None)
    cart_items = request.session.get('cart_items' , None)
    allcategory = Category.objects.all()
    order_obj = Order.objects.get(order_id__iexact =order_id)
    cart_obj = Cart.objects.get(id__iexact = cart_id)
    order_time = DeliveryTime.objects.get(id=delivery_time_id )
    context = {
        "object": order_obj,
        "cart_items" :  cart_items,
        "cart_obj" : cart_obj,
        "cart" : cart_obj,
        "delivery_method" : "Cash On Delivery",
        'delivery_time_id' : order_time
    }
    
    #orders
    order_id_email = order_obj.order_id
    total_amount = order_obj.total
    order_arrival_date = order_time.date 
    order_arrival_time = order_time.get_time_display()
    subject = "Delivery for {}".format(order_id_email)
    from_email = settings.EMAIL_HOST_USER
    to_email = str(order_obj.delivery_address.email)
    message = "Your order was placed successfully Oder Id : f'{order_id_email}' Order Email : f'{to_email}'  Payment Method : Cash On delivery , Payment Amount : f'{total_amount}' Order Arrival Date :  f'{order_arrival_date}' ( f'{order_arrival_time}' ) "
    emailsent = EmailMultiAlternatives(subject=subject, body=message ,from_email=from_email ,  to = [to_email] )
    html_template = get_template("success.html").render(context,request)
    emailsent.attach_alternative(html_template, "text/html")
    emailsent.send()


    
  
    
    return render(request, "success.html", context)


def simulate_mpesa(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode":LipanaMpesaPpassword.Test_c2b_shortcode,
        "CommandID":"CustomerPayBillOnline",
        "Amount":1,
        "Msisdn":254704157038,
        "BillRefNumber":" "
          }
  
    response = requests.post(api_url, json = request, headers=headers)
    return HttpResponse(response.text)

