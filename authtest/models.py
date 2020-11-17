from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    role = models.CharField(max_length=200, default="customer")

    def __str__(self):
        return self.role


class User(AbstractUser):
    full_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.CASCADE)  # role
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
