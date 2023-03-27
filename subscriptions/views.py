from django.shortcuts import render ,redirect, resolve_url ,HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse_lazy  
from django.views.generic import ListView,CreateView,UpdateView,DeleteView ,DetailView
from utils import PAGE_RESULTS, MyPaginator
from django.contrib.auth.mixins import LoginRequiredMixin

###################### Plans Views ##########################

class OffersListView( ListView):
    template_name ="offers.html"
    paginate_by = 4
    paginator_class = MyPaginator # We use our paginator class
    queryset = Plan.objects.all()
    context_object_name = "plans"

class PlanListView(LoginRequiredMixin, ListView):
    template_name ="plans/plan_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Plan.objects.all()
    context_object_name = "plans"

class PlanCreateView(LoginRequiredMixin, CreateView):
    template_name = "plans/plan_create.html"
    form_class = PlanModelForm
    success_url = reverse_lazy('plan-list')

class PlanUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "plans/plan_update.html"
    queryset = Plan.objects.all()
    form_class = PlanModelForm
    success_url = reverse_lazy('plan-list')
    

class PlanDeletetView(LoginRequiredMixin, DeleteView):
    template_name = "plans/plan_delete.html"
    queryset = Plan.objects.all()
    success_url = reverse_lazy('plan-list')
    
    


#################### Subscriptions Views ####################

class SubListView(LoginRequiredMixin, ListView):
    template_name ="subscriptions/sub_list.html"
    paginate_by = PAGE_RESULTS
    paginator_class = MyPaginator # We use our paginator class
    queryset = Subscription.objects.all()
    context_object_name = "subscriptions"

class SubCreateView(LoginRequiredMixin, CreateView):
    template_name = "subscriptions/sub_create.html"
    form_class = SubModelForm
    success_url = reverse_lazy('sub-list')
    
class SubUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "subscriptions/sub_update.html"
    queryset = Subscription.objects.all()
    form_class =  SubModelForm
    success_url = reverse_lazy('sub-list')
    

class SubDeletetView(LoginRequiredMixin, DeleteView):
    template_name = "subscriptions/sub_delete.html"
    queryset =Subscription.objects.all()
    success_url = reverse_lazy('sub-list')

