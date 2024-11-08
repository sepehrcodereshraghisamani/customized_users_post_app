from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
