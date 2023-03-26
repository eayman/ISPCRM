from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
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

class AdminUserAdmin(CustomUserAdmin):
    add_form = AdminCreationForm
    form = AdminChangeForm
    model = Admin

class AgentAdmin(CustomUserAdmin):
    add_form = AgentCreationForm
    form = AgentChangeForm
    model = Agent

class ClientAdmin(CustomUserAdmin):
    add_form = ClientCreationForm
    form = ClientChangeForm
    model = Agent


admin.site.register(Admin,AdminUserAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Client,ClientAdmin)
