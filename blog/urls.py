from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='blog-home'),
]
