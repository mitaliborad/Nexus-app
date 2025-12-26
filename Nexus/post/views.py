from django.shortcuts import render
from .models import Post
from account.models import User
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class PostCreateReadView(ListCreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.all().order_by('-uploaded_at')



