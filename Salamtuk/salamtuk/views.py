from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import SerializerMethodField
from .models import Doctor,Booking, Comment, Patient, Appointment, Attendance, Payment, Clinic
from .serializers import (DoctorSerializers, BookingSerializers , CommentSerializers, PatientSerializer, AppointmentSerializer,
AttendanceSerializer, PaymentSerializer, ClinicSerializer)
from rest_framework import viewsets
from notifications.utils import PushNotifications
# Create your views here.


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers



class AppointmentView(viewsets.ModelViewSet):
    """Powers a form to create a new appointment"""
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

    def create(self, request):
        serializer = BookingSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            PushNotifications(title='title', body='body', user=request.user)
            return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AttendanceView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ClinicView(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
