from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name',"email","appointment")


admin.site.register(Reservation, ReservationAdmin)
