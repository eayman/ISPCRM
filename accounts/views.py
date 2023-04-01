from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import MyPaginator, PAGE_RESULTS
from django.contrib.messages.views import SuccessMessageMixin


from .models import *
from .forms import *

############################################################

class AgentListView(ListView):
    template_name = "agents/agent_list.html"
    queryset = Agent.agents.all()
    context_object_name = "agents"

class AgentProfileView(DetailView):
    template_name = "agents/agent_profile.html"
    queryset = Agent.agents.all()
    context_object_name = "agent"

class AgentCreateView(CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentCreationForm
    success_url = reverse_lazy('agents-list')


class AgentUpdateView(UpdateView):
    template_name = "agents/agent_update.html"
    queryset = Agent.agents.all()
    form_class = AgentChangeForm
    success_url = reverse_lazy('agents-list')

class AgentDeleteView(DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.agents.all()
    context_object_name = "agent"
    success_url = reverse_lazy('agents-list')

############################################################

class ClientListView(LoginRequiredMixin, ListView):
    template_name ="clients/client_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Client.clients.all()
    context_object_name = "clients"

class ClientProfileView(LoginRequiredMixin, DetailView):
    template_name = "clients/client_profile.html"
    queryset = Client.clients.all()
    context_object_name = "client"


class ClientCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientCreationForm
    success_url = reverse_lazy('client-list')
    success_message = "client was created successfully"

   

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "clients/client_update.html"
    queryset = Client.clients.all()
    form_class = ClientChangeForm
    success_url = reverse_lazy('client-list')
    


class ClientDeleteView(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.clients.all()
    context_object_name = "client"
    success_url = reverse_lazy('client-list')

class ClientDeletetView(LoginRequiredMixin, DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.clients.all()
    context_object_name = "client"
    success_url = reverse_lazy('client-list')

############################################################

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm