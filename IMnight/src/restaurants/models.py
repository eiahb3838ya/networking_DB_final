from django.db import models
from my_user.models import Profile
# Create your models here.


class Restaurant(models.Model):
    """docstring for Restaurant"""
    
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(
        max_length=120, null=True, blank=True)
    guests = models.ManyToManyField(Profile, through='BeenRestaurant')
    # slug = models.SlugField(null=True, blank=True)
    # coupon = models.CharField(max_length=120, null=True, blank=True)
    # coupon_due = models.DurationField(null=True, blank=True)
    # photo = models.FileField()

    def __str__(self):
        return self.name

class BeenRestaurant(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    times =models.PositiveIntegerField(default=0)

    def __str__(self):
        return (self.user.user.username + " has been to " + self.restaurant.name + " " + str(self.times) + " " + "times")
