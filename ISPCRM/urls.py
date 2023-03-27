from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("leads.urls")),
    ###############################################
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('contact-us',TemplateView.as_view(template_name="contact.html"),name='contact-us'),
    
]