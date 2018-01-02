from django.conf.urls import url
from django.conf.urls import url
from django.contrib.auth.views import login, logout  # 利用內建的view funciton

from .views import (
    HomeView,
    UserCreateView
)
urlpatterns = [

    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^create$', UserCreateView.as_view(),name='create'),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
]
