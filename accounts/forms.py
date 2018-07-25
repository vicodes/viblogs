from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class SignupForm(UserCreationForm):
    first_name  = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("first_name", "username", "email", "password1", "password2")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
 
