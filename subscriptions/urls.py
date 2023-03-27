from django.urls import path
from .views import *

urlpatterns = [
    
    ##################################### Plans URLs #########################################
    path('plans/', PlanListView.as_view(),name='plan-list'),
    path('plans/create',PlanCreateView.as_view(),name='plan-create'),
    path('plans/<int:pk>/update/',PlanUpdateView.as_view(), name='plan-update'),
    path('plans/<int:pk>/delete/',PlanDeletetView.as_view(), name='plan-delete'),
    
    ################################ Subscriptions URLs ######################################
    path('subscriptions/', SubListView.as_view(),name='sub-list'),
    path('subscriptions/create',SubCreateView.as_view(),name='sub-create'),
    path('subscriptions/<int:pk>/update/',SubUpdateView.as_view(), name='sub-update'),
    path('subscriptions/<int:pk>/delete/',SubDeletetView.as_view(), name='sub-delete'),
    
]