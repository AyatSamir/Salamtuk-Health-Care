from django.shortcuts import render
from fcm_django.models import FCMDevice
from .serializers import NotificationSerializer
from rest_framework import viewsets
from .models import Notification
# Create your views here.


class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

