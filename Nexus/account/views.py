from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

# Create your views here.
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]



