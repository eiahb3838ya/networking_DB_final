"""imnight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from views import index
# from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^', include('menu.urls', namespace='menu')),
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('my_user.urls', namespace='profiles')),
    url(r'^drawprice/',include('drawprice.urls', namespace='drawprice')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^coupons/',include('draw_restaurant.urls', namespace='draw_restaurant')),

    # url(r'^accounts/login/$',login),
    # url(r'^accounts/logout/$',logout),
    # url(r'^index/$',index),
]
