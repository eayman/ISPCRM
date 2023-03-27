from django.urls import path
from .views import *

urlpatterns = [
    #### Lead URLs
    path('leads/',LeadListView.as_view(),name='lead-list'),
    path('leads/create',LeadCreateView.as_view(),name='lead-create'),
    path('leads/<int:pk>/update/',LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:pk>/delete/',LeadDeleteView.as_view(), name='lead-delete'),
]
