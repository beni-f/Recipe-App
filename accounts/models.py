from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
        Custom User Creation Model
    """
    bio = models.TextField(max_length=255, null=True, blank=True)

