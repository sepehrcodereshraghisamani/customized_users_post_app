from django.urls import path
from .views import CustomUserCreationView
from . import views

urlpatterns = [
    path('register/', CustomUserCreationView.as_view(), name='signup'),
    path('logout/', views.custom_logout, name='custom_logout'),
]

