from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class HomeView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to Nexus API"}, status=status.HTTP_200_OK)