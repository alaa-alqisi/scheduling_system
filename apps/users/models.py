from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    username = models.TextField(blank=False,default="", max_length=255, verbose_name="username")

    # USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"