from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
class HomeView(TemplateView):
	template_name = 'home.html'

# class LoginView(TemplateView):
# 	template_name = 'login.html'

class UserCreateView(CreateView):
	form_class=UserCreationForm
	template_name='signup.html'
	success_url='/menu'
