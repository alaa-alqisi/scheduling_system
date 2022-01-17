from django.utils import timezone
from django.db import models
from apps.appointments.models import Appointment
from apps.utils.models import Timestamps


class Reservation(Timestamps):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=100,blank=False,verbose_name='email address')
    full_name=models.CharField(blank=False,max_length=100)


