from django import forms
from .models import Address,DeliveryTime
from django.contrib.admin.widgets import AdminDateWidget

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line1','address_line2','city','name','email','phone','postal_code']
        widgets = {
            'name':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Name", "class":"form-control input-md", "required":""
                }
            ),
            'email':forms.TextInput(
                attrs = {
                     " type":"email", "placeholder":"Email Address", "class":"form-control input-md", "required":""
                }
            ),
             'address_line1':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Address", "class":"form-control input-md", "required":""
                }
            ),
             'address_line2':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Street Address", "class":"form-control input-md", "required":""
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
                'postal_code':forms.TextInput(
                attrs = {
                     " type":"text", "placeholder":"Postal Code", "class":"form-control input-md", "required":""
                }
            ),
        }


class DeliveryTimeAddress(forms.ModelForm):
    class Meta:
        model = DeliveryTime
        fields = ['date' , 'time']
        widgets  = {
             'date' : AdminDateWidget()
             
                
         }




       