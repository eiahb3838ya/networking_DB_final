from django.conf.urls import url
from django.conf.urls import url

from .views import (
    ProfileDetail,
    ProfileUpdateView
)
urlpatterns = [

    url(r'^$', ProfileDetail.as_view(), name='detail'),
    url(r'^update$', ProfileUpdateView.as_view(), name='update'),
    # url(r'^create$', RestaurantCreateView.as_view(), name='create'),
]
