from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username","password1","password2")

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ("first_name", "last_name","username", "email","NID","phone_number")


class AdminCreationForm(CustomUserCreationForm):

    class Meta(CustomUserCreationForm):
        model = Admin
        fields = ("username","password1","password2")
    

class AdminChangeForm(CustomUserChangeForm):
    
    class Meta(CustomUserChangeForm):
        model = Admin
        fields = ("first_name", "last_name","username", "email","NID","phone_number")

class AgentCreationForm(CustomUserCreationForm):

    class Meta(CustomUserCreationForm):
        model = Agent
        fields = ("username","password1","password2")

class AgentChangeForm(CustomUserChangeForm):
    
    class Meta(CustomUserChangeForm):
        model = Agent
        fields = ("first_name", "last_name","username", "email","NID","phone_number")
       



class ClientCreationForm(CustomUserCreationForm):

    class Meta(CustomUserCreationForm):
        model = Client
        fields = ("username","password1","password2")

class ClientChangeForm(CustomUserChangeForm):
    class Meta(CustomUserChangeForm):
        model = Client
        fields = ("first_name", "last_name","username", "email","NID","phone_number")
