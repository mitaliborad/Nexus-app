from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(("email address"), unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)   

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
    



