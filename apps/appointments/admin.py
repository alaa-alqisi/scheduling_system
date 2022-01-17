from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'interval')


admin.site.register(Appointment, AppointmentAdmin)