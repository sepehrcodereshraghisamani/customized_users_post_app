from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect



# Create your views here.
class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or any other page you prefer
