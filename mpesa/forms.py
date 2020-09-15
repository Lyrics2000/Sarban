from django import forms

class CashAtHand(forms.Form):
    cash_at_hand = forms.IntegerField(widget=forms.NumberInput(
        attrs={  "type": "number"  , "placeholder" : "Enter the Cash At Hand In Order To get Change" , "class" : "form-control lgn_input" 
        
        }
    ))
    