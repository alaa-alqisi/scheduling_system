from django.utils import timezone
from django.db import models
from apps.users.models import User
from apps.utils.models import Timestamps


class Appointment(Timestamps):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False,default=timezone.now())
    intervals = (
        (1, '15 minutes'),
        (2, '30 minutes'),
        (3, '45 minutes'),
    )
    interval = models.IntegerField(choices=intervals, default=1)


