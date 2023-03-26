from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import *
from .forms import *


class UserListView(ListView):
    template_name = "agents/agent_list.html"
    queryset = CustomUser.objects.all()
    context_object_name = "users"

class UserProfileView(DetailView):
    template_name = "agents/agent_profile.html"
    queryset = CustomUser.objects.all()
    context_object_name = "user"

class UserCreateView(CreateView):
    template_name = "agents/agent_create.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('agents-list')

class UserUpdateView(UpdateView):
    template_name = "agents/agent_update.html"
    queryset = CustomUser.objects.all()
    form_class = CustomUserChangeForm
    print("ok")
    success_url = reverse_lazy('agents-list')
    print("ok")

class UserDeleteView(DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = CustomUser.objects.all()
    context_object_name = "user"
    success_url = reverse_lazy('agents-list')
    
