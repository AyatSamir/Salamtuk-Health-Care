from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_doctor = models.BooleanField(default=0)
    description = models.TextField()
    address = models.TextField()
    photo = models.ImageField(upload_to='uploads/%Y-%m-%d/', max_length=100)
    mobile_phone = PhoneNumberField(null=False, blank=False)#, unique=True)
    country = CountryField(blank_label='(Select Country)')
    city = models.CharField(max_length=200) # question



#This signal used to create user profile after registeration process
@receiver(post_save, sender=User)
def creat_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)