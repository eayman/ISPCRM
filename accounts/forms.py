from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
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


#############################################################

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'User Name',
                'type': 'username',
                'name' : 'username',
                'id': 'username',
                'class': 'w-full py-4 px-8 bg-slate-200 placeholder:font-semibold rounded hover:ring-1 outline-blue-500'
            }
        )
    )

    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'Password',
                'type': 'password',
                'name' : 'password',
                'id': 'password',
                'class': 'w-full py-4 px-8 bg-slate-200 placeholder:font-semibold rounded hover:ring-1 outline-blue-500'
            }
        )
    )
