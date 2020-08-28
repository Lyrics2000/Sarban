from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

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
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('UserName')
        password = self.cleaned_data.get('Password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)
    

 




class RegisterForm(forms.Form):
    firstName = forms.CharField(
        widget=forms.TextInput(
            attrs={
               "name" : "fullname" , "type":"text" , "placeholder":"First Name",  "class":"form-control lgn_input"
               , "required":" "
            }
        )
    )
    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
               "name" : "fullname" , "type":"text" , "placeholder":"Last Name",  "class":"form-control lgn_input"
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
    
    password = forms.CharField(
        widget=forms.PasswordInput(
           attrs={ "type":"password" ,"placeholder":"Password", "class":"form-control lgn_input",
            "required":""}
        )
    )
    confirmpassword = forms.CharField(
        widget=forms.PasswordInput(
          attrs={  "type":"password" ,"placeholder":"Confirm Password", "class":"form-control lgn_input",
            "required":""
          }
        )
    )
    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = User.objects.filter(username = username)
    #     if qs.exists:
    #         raise forms.ValidationError("User Name exists")
    #     return username
    def clean_everything(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username = username)
        
        if qs.exists:
            raise forms.ValidationError("User Name exists")
        else:
            password = self.cleaned_data.get('password')
            confirmpassword = self.cleaned_data.get('confirmpassword')
            if password != confirmpassword:
                raise forms.ValidationError("Password must match")
            email = self.cleaned_data.get('email')
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError(
                    "This email has already been registered")
        return super(RegisterForm, self).clean(*args, **kwargs)
    # def clean(self):
    #     password = self.password
    #     password2 = self.confirmpassword
    
    #     if password != password2:
    #         raise forms.ValidationError("Passwords Do Not Match")
        
    #     return data