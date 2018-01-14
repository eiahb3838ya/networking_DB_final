from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Restaurant
# Create your views here.


class RestraurantListView(ListView):
    model=Restaurant
    template_name = "restaurants_lists.html"
    def get_context_data(self, **kwargs):
        context = super(RestraurantListView, self).get_context_data(**kwargs)
        context['thisuser'] = self.request.user.pk
        print(context['thisuser'])
        return context

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)

    
