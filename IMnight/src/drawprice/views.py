from django.shortcuts import render
from django.views.generic import TemplateView

class DrawingView(TemplateView):
	template_name = 'draw.html'

class PrizeView(TemplateView):
	template_name = 'prize.html'
# class LoginView(TemplateView):
# 	template_name = 'login.html'

