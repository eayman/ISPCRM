from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("first_name", "last_name","username", "email","NID","phone_number","password1","password2")

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ("first_name", "last_name","username", "email","NID","phone_number")
