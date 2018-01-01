from django.conf.urls import url

from .views import (
    ProfileDetail
)
urlpatterns = [

    url(r'^(?P<pk>\d+)/$', ProfileDetail.as_view(), name='detail'),
    
]
