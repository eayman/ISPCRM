from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
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

class ClientListView(ListView):
    template_name = "clients/client_list.html"
    queryset = Client.clients.all()
    context_object_name = "clients"

class ClientProfileView(DetailView):
    template_name = "clients/client_profile.html"
    queryset = Client.clients.all()
    context_object_name = "client"

class ClientCreateView(CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientCreationForm
    success_url = reverse_lazy('clients-list')

class ClientUpdateView(UpdateView):
    template_name = "clients/client_update.html"
    queryset = Client.clients.all()
    form_class = ClientChangeForm
    success_url = reverse_lazy('clients-list')

class ClientDeleteView(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.clients.all()
    context_object_name = "client"
    success_url = reverse_lazy('clients-list')
    
############################################################
