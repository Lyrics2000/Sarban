from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class GuestForm(forms.Form):
    email = forms.EmailField()
class LogiForm(forms.Form):
    UserName = forms.CharField(widget=forms.TextInput(
        attrs={"name": "phone" ,  "type": "text"  , "placeholder" : "Enter  UserName" , "class" : "form-control lgn_input" 
        ,  "required": ""
        }
    ))

    Password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "name" : "password1",
            " type" : "password",
             "placeholder" : "Enter Password", 
             " class" : "form-control lgn_input", 
              "required" : ""
        }
    ))


class RegisterForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(
            attrs={
               "name" : "fullname" , "type":"text" , "placeholder":"Full name",  "class":"form-control lgn_input"
               , "required":" "
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type":"text" , "placeholder":"UserName",  "class":"form-control lgn_input"
               , "required":" "
            }
        )
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "name":"emailaddress", "type":"email" , "placeholder":"Email Address", "class":"form-control lgn_input",
             "required":""

        }
    ))
    phoneNumber  = forms.CharField(
        widget=forms.TextInput(
            attrs={
               "name":"phone", "type":"text", "placeholder":"Phone Number", "class":"form-control lgn_input",
                "required":""  
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={ "type":"password" ,"placeholder":"New Password", "class":"form-control lgn_input",
            "required":""}
        )
    )
    confirmpassword = forms.CharField(
        widget=forms.PasswordInput(
          attrs={  "type":"password" ,"placeholder":"New Password", "class":"form-control lgn_input",
            "required":""
          }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)
        if qs.exists:
            raise forms.ValidationError("User Name exists")
        return username
    # def clean(self):
    #     password = self.password
    #     password2 = self.confirmpassword
    
    #     if password != password2:
    #         raise forms.ValidationError("Passwords Do Not Match")
        
    #     return data