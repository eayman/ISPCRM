from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "first_name", "last_name","email","NID","phone_number"]
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ("NID","phone_number")}),
    ) #this will allow to change these fields in admin module


admin.site.register(CustomUser, CustomUserAdmin)