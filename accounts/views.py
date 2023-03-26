from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import *
from .forms import *


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
    
