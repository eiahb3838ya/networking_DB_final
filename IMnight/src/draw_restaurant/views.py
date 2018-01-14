from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from restaurants.models import Restaurant
from .models import Coupon
from .form import CouponForm
import random
# Create your views here.

class DrawRestaurantListView(ListView):
    model = Coupon
    template_name = "draw_restaurant_list.html"
    def get_queryset(self):
        queryset = super(DrawRestaurantListView, self).get_queryset()
        # print(self.request.user.profile)
        return Coupon.objects.filter(owner=self.request.user.profile)

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Coupon, owner=user)

# @login_required()
def draw_restaurant_createview(request):
    form = CouponForm()
    if request.method == "POST":
        form = CouponForm(request.POST)
        if request.user.is_authenticated():
            instance=form.save(commit=False)
            instance.owner = request.user.profile
            
            random_num = random.randrange(Restaurant.objects.count())
            print(random_num)
            instance.restaurant = Restaurant.objects.all()[random_num]
            form.save()
            # obj= RestaurantLocation.objects.create(
            #       name=form.cleaned_data.get("name"),
            #       location=form.cleaned_data.get("location"),
            #       category=form.cleaned_data.get("category"),
            # )
            return HttpResponseRedirect("/coupons")
        else:
            return HttpResponseRedirect("/login")
        if form.errors:
            print("form.errors",form.errors)
    template_name="draw_restaurant_create.html"
    context={'form':form}
    return render(request,template_name,context)
        
