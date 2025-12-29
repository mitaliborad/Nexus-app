from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class CommentCreateReadView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def get_queryset(self):
        return Comment.objects.all().order_by('-commented_at')
    
class CommentUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'id'