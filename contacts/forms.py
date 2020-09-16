from django import forms
from .models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['full_name' , 'email_address','subject','message',]
        widgets = {
            'full_name' : forms.TextInput(
                attrs={
                   " class":"prompt srch_explore" ,"type":"text",   "required":"" ,"placeholder":"Your Full"	
                    
                }
            ),
            'email_address' : forms.EmailInput(
                attrs={
                    "class":"prompt srch_explore", "type":"email"," required":"" ,"placeholder":"Your Email Address"
                }
            ),
            'subject' : forms.TextInput(
                attrs={
                   "class":"prompt srch_explore", "type":"text","required":"", "placeholder":"Subject"	
                    
                }
            ),
            'message' :  forms.Textarea(
                attrs={
                    "rows":"2" ,"class":"form-control" , "required":"" ,"placeholder":"Write Message"
                }
            )
            
        }