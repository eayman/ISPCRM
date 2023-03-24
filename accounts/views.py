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
    queryset = Agent.objects.all()
    context_object_name = "agent"

class AgentCreateView(CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentCreationForm
    def get_success_url(self):
        return resolve_url("agents-list")

class AgentUpdateView(UpdateView):
    print("start")
    template_name = "agents/agent_update.html"
    queryset = AgentProfile.agents.all()
    #form_class = CustomUserChangeForm
    form_class = AgentUpdateForm
    def get_success_url(self):
        return resolve_url("agents-list")
    
    print("end")

def agent_update(request,pk):
    agent = get_object_or_404(AgentProfile,id=pk)
    #user = agent.user
    form = AgentUpdateForm(instance=agent)
    #form = UserChangeForm(isinstance=user)
    if request.method == "POST":
        form = AgentUpdateForm(request.POST,instance=agent)
        #form = UserChangeForm(request.POST, isinstance=user)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
    context = {
        'form':form  

    }
    return render(request,"agents/agent_update.html",context)

class AgentDeleteView(DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.agents.all()
    context_object_name = "agent"
    def get_success_url(self):
        return resolve_url("agents-list")
