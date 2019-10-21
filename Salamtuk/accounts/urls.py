from django.contrib import admin
from django.urls import path, include
from accounts.views import UserProfileAPIView, CustomLoginView

from rest_auth.views import (LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView, LogoutView)
from rest_auth.registration.views import RegisterView, VerifyEmailView

from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('user-profile/', UserProfileAPIView.as_view(), name='user_profile'),
    path('', include('rest_auth.urls')), # logout/login
    path('registration/', include('rest_auth.registration.urls')), # registeration
    #path('', include('django.contrib.auth.urls')),
    path('login/', CustomLoginView.as_view(), name='custom_login')

]
