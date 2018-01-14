from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Restaurant
# Create your views here.


class RestraurantListView(ListView):
    model=Restaurant
    template_name = "restaurants_lists.html"
    
