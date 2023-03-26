from django.urls import path

from .views import *

urlpatterns = [
    ############# Agent URLs #############
    path("agents/",AgentListView.as_view(),name="agents-list"),
    path("agents/create",AgentCreateView.as_view(),name="agent-create"),
    path("agents/<int:pk>/profile",AgentProfileView.as_view(),name="agent-profile"),
    path("agents/<int:pk>/update",AgentUpdateView.as_view(),name="agent-update"),
    path("agents/<int:pk>/delete",AgentDeleteView.as_view(),name="agent-delete"),
    ############# Client URLs #############
    path("clients/",ClientListView.as_view(),name="clients-list"),
    path("clients/create",ClientCreateView.as_view(),name="client-create"),
    path("clients/<int:pk>/profile",ClientProfileView.as_view(),name="client-profile"),
    path("clients/<int:pk>/update",ClientUpdateView.as_view(),name="client-update"),
    path("clients/<int:pk>/delete",ClientDeleteView.as_view(),name="client-delete"),
    
]