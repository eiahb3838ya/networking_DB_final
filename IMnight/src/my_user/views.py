from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import ProfileForm
# Create your views here.
User = get_user_model()
from django.contrib.auth.decorators import login_required


class ProfileDetail(LoginRequiredMixin,DetailView):
    model = Profile

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    template_name = 'profiles/profile_detail.html'
    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/update.html"
    success_url = "/profiles"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileUpdateView,
                        self).get_context_data(*args, **kwargs)
        context["title"] = 'Edit your profile'
        return context

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Profile, user=user)

    def get_queryset(self):
        queryset = Profile.objects.filter(user=self.request.user)
        return queryset





    
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetail, self).get_context_data(**kwargs)
    #     print(context)
    #     return context
    
