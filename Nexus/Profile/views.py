from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserProfileSerializer
from account.models import User
from rest_framework.permissions import IsAuthenticated

class UserProfileView(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated] 
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
