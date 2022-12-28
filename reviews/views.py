from django.shortcuts import render
from django.views.generic import ListView
from .models import Review

# Create your views here.
class HomePageView(ListView):
    template_name = "home.html"
    model = Review
