from django.urls import path

from .views import *

urlpatterns = [
    ############# Agent URLs #############
    path("agents/",AgentListView.as_view(),name="agents-list"),
    path("agents/create",AgentCreateView.as_view(),name="agent-create"),
    path("agents/<int:pk>/profile",AgentProfileView.as_view(),name="agent-profile"),
    path("agents/<int:pk>/update",AgentUpdateView.as_view(),name="agent-update"),
    #path("agents/<int:pk>/update",agent_update,name="agent-update"),
    
    path("agents/<int:pk>/delete",AgentDeleteView.as_view(),name="agent-delete"),
    ############# Client URLs #############
    
]