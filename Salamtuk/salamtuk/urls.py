from django.urls import path, include
from rest_framework import routers
from salamtuk import views

router = routers.DefaultRouter()
router.register('doctors', views.DoctorView)
router.register('appointments', views.AppointmentView)
router.register('bookings', views.BookingView)
router.register('comments', views.CommentView)
router.register('patients', views.PatientView)
router.register('attendances', views.AttendanceView)
router.register('payments', views.PaymentView)
router.register('clinics', views.ClinicView)







urlpatterns = [
    path('', include(router.urls)),
]