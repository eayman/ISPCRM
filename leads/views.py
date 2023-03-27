from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView 
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy  
from utils import MyPaginator, PAGE_RESULTS
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.shortcuts import get_object_or_404


class LeadListView(LoginRequiredMixin,ListView):
    template_name = "leads/lead_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    
    def get_queryset(self):
        queryset = Lead.objects.all()
        return queryset
        
    context_object_name = "leads"

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    success_url = reverse_lazy('lead-list')
   
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    success_url = reverse_lazy('lead-list')
    
class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    success_url = reverse_lazy('lead-list')

def change_contacted_status(LoginRequiredMixin, request,pk):
    lead = get_object_or_404(Lead,id=pk)
    lead.is_contacted = not(lead.is_contacted)
    lead.save()
    return HttpResponse()
