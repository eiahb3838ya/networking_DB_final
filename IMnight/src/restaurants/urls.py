from django.conf.urls import url


from .views import (
    RestraurantListView
    
)
urlpatterns = [
    url(r'^$', RestraurantListView.as_view(), name='list'),
    
]
