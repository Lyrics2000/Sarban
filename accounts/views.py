from django import forms
from django.contrib.auth import authenticate,login,get_user_model
from django.shortcuts import render,redirect
from .forms import LogiForm,RegisterForm,GuestForm
from django.utils.http import is_safe_url
from .models import GuestEmail
from django.contrib.auth.models import User

# Create your views here.

def guest_register_view(request):
    login_form = GuestForm(request.POST or None)
    context = {
        'login' : login_form
    }
    next = request.GET.get('next')
    next_post = request.GET.get('next')
    redirect_path = next or next_post or None
    if login_form.is_valid:
        email = request.POST.get("email")
        new_guest_email = GuestEmail.objects.create(email = email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path,request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/account/signup/")
        
    
    return redirect("/account/signup/")

def signin(request):
    login_form = LogiForm(request.POST or None)
    context = {
        'login' : login_form
    }
    next = request.GET.get('next')
    next_post = request.GET.get('next')
    redirect_path = next or next_post or None
    if login_form.is_valid:
        username = request.POST.get("UserName")
        password = request.POST.get('Password')
        user = authenticate(request,username = username, password = password )
        if user is not None:
            login(request,user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            
            if is_safe_url(redirect_path,request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # return redirect("accounts:signin")
            pass
    
    return render(request,'signin.html',context)


def signup(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form' : form
    }
    # if form.is_valid:
    #     if request.POST.get('password') != request.POST.get('confirmpassword'):
    #         raise forms.ValidationError("Passwords Do Not Match")
    #     fullname = request.POST.get("fullName")
    #     username = request.POST.get("username")
    #     email = request.POST.get("email")
    #     phoneNumber = request.POST.get("phoneNumber")
    #     password = request.POST.get("password")

    #     new_user = User.objects.create_user(username = username ,email = email,password = password)
    #     print(new_user)
    next = request.GET.get('next')
    next_post = request.GET.get('next')
    redirect_path = next or next_post or None
    if form.is_valid:
        if request.POST:
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User.objects.create_user(username = username , email = email , password = password)
            user.last_name = lastName
            user.first_name = firstName
            user.save()
            userr = authenticate(request,username = username, password = password )
            if userr is not None:
                login(request,userr)
                try:
                    del request.session['guest_email_id']
                except:
                    pass
                
                if is_safe_url(redirect_path,request.get_host()):
                    return redirect(redirect_path)
                else:
                    return redirect("/")
            else:
                # return redirect("accounts:signin")
                pass


        
    return render(request,'signup.html',context)