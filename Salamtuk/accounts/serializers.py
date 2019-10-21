from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import UserProfile
from django_countries.serializer_fields import CountryField
from rest_auth.views import LoginView
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.validators import UniqueValidator

class UserProfileSerializer(serializers.ModelSerializer):
    country = CountryField()
    class Meta:
        model = UserProfile
        fields ='__all__'


class CustomLoginView(LoginView):
    phone_number = PhoneNumberField()