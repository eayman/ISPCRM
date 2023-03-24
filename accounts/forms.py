from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",)


class AgentCreationForm(CustomUserCreationForm):
    class Meta:
        model = AgentProfile
        fields = ("username", "email")

class AgentUpdateForm(CustomUserChangeForm):
    class Meta:
        model = AgentProfile
        fields = ("first_name", "last_name", "username", "email")
        exclude = ("password",)
