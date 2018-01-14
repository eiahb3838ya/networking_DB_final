from django.db import models

# Create your models here.


class Restaurant(models.Model):
    """docstring for Restaurant"""
    
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(
        max_length=120, null=True, blank=True)
    # slug = models.SlugField(null=True, blank=True)
    # coupon = models.CharField(max_length=120, null=True, blank=True)
    # coupon_due = models.DurationField(null=True, blank=True)
    # photo = models.FileField()

    def __str__(self):
        return self.name
