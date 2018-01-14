from django.conf.urls import url


from .views import (
    DrawRestaurantListView, draw_restaurant_createview)
urlpatterns = [

    url(r'^$', DrawRestaurantListView.as_view(), name='coupons'),
    url(r'^draw$', draw_restaurant_createview, name='list'),
    
]
