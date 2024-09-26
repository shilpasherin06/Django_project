from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        # widgets = {
        #     "Brand_name": forms.TextInput(attrs={'class': 'form-control',"placeholder": "Enter Brand Name"}),
        #     "Model_name": forms.TextInput(attrs={'class': 'form-control',"placeholder": "Enter Model Name"}),
        #     "price": forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Enter Price"}),
        #     "gst": forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Enter GST"}),
        #     "final_price": forms.NumberInput(attrs={'class': 'form-control',"placeholder": "Enter Final Price"}),
        #     "picture": forms.FileInput(attrs={'class': 'form-control',"placeholder": "Upload Image"}),
            
        # }