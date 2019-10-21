from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User,related_name='notifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
