from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_ref','customer_ref','order_date','quantity']

        # widgets = {
        #     "product_ref": forms.TextInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        #     "customer_ref": forms.TextInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        #     "order_date": forms.DateInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        #     "quantity": forms.NumberInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        #     "price": forms.NumberInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        #     "gst": forms.NumberInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        #     "final_price": forms.NumberInput(attrs={"class": "form-control","placeholder":"Enter product name"}),
        # }

        

        