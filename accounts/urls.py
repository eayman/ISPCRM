from django.urls import path

from .views import *

urlpatterns = [
    ############# Agent URLs #############
    path("agents/",UserListView.as_view(),name="agents-list"),
    path("agents/create",UserCreateView.as_view(),name="agent-create"),
    path("agents/<int:pk>/profile",UserProfileView.as_view(),name="agent-profile"),
    path("agents/<int:pk>/update",UserUpdateView.as_view(),name="agent-update"),
    #path("agents/<int:pk>/update",agent_update,name="agent-update"),
    
    path("agents/<int:pk>/delete",UserDeleteView.as_view(),name="agent-delete"),
    ############# Client URLs #############
    
]