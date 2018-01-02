from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    # facebook = models.
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    OTHER='OR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (OTHER, 'other'),
    )
    grade = models.CharField(max_length=2,
                             choices=YEAR_IN_SCHOOL_CHOICES,
                             default=FRESHMAN, 
                             null=False, 
                             blank=True)
    point = models.IntegerField(default=100)
    sign_in_date = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    # performer    = models.BooleanField(default=False)
    


def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
