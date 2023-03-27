from django.forms import ModelForm
from .models import *
from django import forms


class SubModelForm(ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
        
    def __init__(self, *args, **kwargs ):
        super(SubModelForm,self).__init__(*args, **kwargs)
        
        for label, field in self.fields.items():
            field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        

class PlanModelForm(ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"
        
    def __init__(self, *args, **kwargs ):
        super(PlanModelForm,self).__init__(*args, **kwargs)
        
        for label, field in self.fields.items():
            field.widget.attrs.update({'class':'mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"',})
        

