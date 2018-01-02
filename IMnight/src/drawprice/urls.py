from django.conf.urls import url
from django.conf.urls import url

from .views import (
    DrawingView,
    PrizeView
)
urlpatterns = [

    url(r'^draw$', DrawingView.as_view(),name='draw'),
    url(r'^prize$', PrizeView.as_view(),name='prize'),
]