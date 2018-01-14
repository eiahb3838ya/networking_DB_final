from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from my_user.models import Profile
from restaurants.models import Restaurant

# Create your models here.
class Coupon(models.Model):
    owner = models.ForeignKey(
        'my_user.Profile', related_name='own_coupon', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        'restaurants.Restaurant', related_name='give_out_coupon', on_delete=models.CASCADE)
    discount = models.FloatField(default=0.8,  null=True, blank=True)
    drawtime = models.DateTimeField(auto_now_add=True)
    # due= models.DurationField(default=)
    # performer    = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    def __str__(self):
        return (self.owner.user.username + "got"+ self.restaurant.name)
    @property
    def title(self):
    	return self.restaurant.name

# def __str__(self):
#         return self.restaurant.name




def __unicode__(self):
        return "%s has a  %s coupon" % (self.owner, self.restaurant)

