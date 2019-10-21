from django.urls import path, include
from notifications import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('notifications', views.NotificationView)



urlpatterns = [
    path('', include(router.urls)),
]