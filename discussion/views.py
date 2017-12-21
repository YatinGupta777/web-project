from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from discussion.models import *
# Create your views here.
class AdvicesView(ListView):
    context_object_name = 'advices_list'
    model = Advices
