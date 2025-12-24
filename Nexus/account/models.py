from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        print(refresh)
        return{
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }
    



