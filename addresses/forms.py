from django import forms
from .models import Address,DeliveryTime
from django.contrib.admin.widgets import AdminDateWidget

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line1','address_line2','city','name','email','phone','estate_decsription']
        widgets = {
            'name':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Name", "class":"form-control input-md", "required":""
                }
            ),
            'estate_decsription':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Description", "class":"form-control input-md", "required":""
                }
            ),
            'email':forms.TextInput(
                attrs = {
                     " type":"email", "placeholder":"Email Address", "class":"form-control input-md", "required":""
                }
            ),
             'address_line1':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Enter Location", "class":"form-control input-md", "required":"","id" : "search_id"
                }
            ),
             'address_line2':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"eg. Waruku House", "class":"form-control input-md", "required":""
                }
            ),
             'city':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"City", "class":"form-control input-md", "required":""
                }
            ),
              'phone':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Phone Number", "class":"form-control input-md", "required":""
                }
            ),
               
        }


class DeliveryTimeAddress(forms.ModelForm):
    class Meta:
        model = DeliveryTime
        fields = ['date' ]
        widgets  = {
             'date' : forms.DateInput(
                 attrs={
                     "type":"datetime-local", "id":"birthdaytime" ,"name":"birthdaytime","class":"form-control"
                 }
             )
    
         }




       