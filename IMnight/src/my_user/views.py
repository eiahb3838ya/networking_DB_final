from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Profile
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()
class ProfileDetail(DetailView):
    model = Profile

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    template_name = 'profiles/profile_detail.html'
    def get_object(self):
        user = self.kwargs['pk']
        return get_object_or_404(Profile, user=user)
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        print(context)
        return context
    
