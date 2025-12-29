from django.shortcuts import render
from .models import Post, Like
from account.models import User
from .serializers import PostSerializer, LikeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PostCreateReadView(ListCreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Post.objects.all().order_by('-uploaded_at')
    
class PostUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

class PostLikesView(ListCreateAPIView):
    serializer_class = LikeSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def post(self, request):
        user = request.user
        post_id = request.data.get('post_id')
        post = Post.objects.get(id=post_id)
        
        exist_like = Like.objects.filter(post_id=post, user_id=user).first()

        if exist_like:
            exist_like.delete()
            total = Like.objects.filter(post_id=post, like=True).count()
            return Response({'action': 'unliked', 'total_likes': total}, status=status.HTTP_200_OK)
        else:
            like = Like.objects.create(post_id=post, user_id=user, like=True)
            serializer = self.get_serializer(like, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
