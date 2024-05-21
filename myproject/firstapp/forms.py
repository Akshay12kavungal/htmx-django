from django import forms
from .models import Contact
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields='__all__'


class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    phone_number=forms.CharField(max_length=10)
    email=forms.EmailField()
    

    

    class Meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name','phone_number')

        