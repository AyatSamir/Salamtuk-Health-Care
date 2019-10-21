from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from salamtuk.utilities import SPECIALIZED_TYPES, PAYMENT_TYPE

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    title = models.TextField()
    description = models.TextField()
    specialized = models.CharField(max_length=100,choices=SPECIALIZED_TYPES)


    def __str__(self):
        return self.name


class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='Doctor_appointment')
    working_days = models.DateField()
    time_days = models.TimeField()




class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name="Doctor_Booking")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='Patient_Booking')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='Appointment')


class Comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     comment = models.TextField()
     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='Comment')


class Attendance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='Patient_Attendance')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='Booking_Attendance')
    is_attend = models.BooleanField()


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='Patient_Payment')
    payment_type = models.CharField(max_length=50,choices=PAYMENT_TYPE)


class Clinic(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_clinic')
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    services = models.TextField()


