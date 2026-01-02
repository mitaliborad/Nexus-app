from rest_framework import serializers
from account.models import User
from post.models import Post
from post.serializers import PostSerializer
from post.models import Like


class UserProfileSerializer(serializers.ModelSerializer):
    liked_posts = serializers.SerializerMethodField()
    created_posts = serializers.SerializerMethodField()

    def get_created_posts(self, obj):
        user_posts = Post.objects.filter(user=obj)
        return PostSerializer(user_posts, many=True).data
    
    def get_liked_posts(self, obj):
        liked_post_ids = Like.objects.filter(user_id=obj, like=True).values_list('post_id', flat=True)
        liked_posts = Post.objects.filter(id__in=liked_post_ids)
        return PostSerializer(liked_posts, many=True).data
    
    class Meta:
        model = User
        fields = ['username', 'bio', 'profile_picture', 'created_posts', 'liked_posts']