from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    discipline = models.CharField(max_length=255)
    user_group = models.CharField(max_length=100)
    
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "discipline", "user_group"]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email