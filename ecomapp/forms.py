# myapp/forms.py
from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','discription','price','image']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField( required=True)
    class meta:
        model=User
        fields= ['username','email','password1','password2']
        labels={
            'username':'Username',
            'email':'Email Address',
            'password1':'Password',
            'password2':'Confirm Password',
        }        