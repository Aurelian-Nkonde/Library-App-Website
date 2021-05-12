from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    lastName = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username