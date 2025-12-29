from rest_framework import serializers
from .models import Post, Like
from account.models import User
from django.core.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return User.objects.get(id=obj.user.id).username
    
    class Meta:
        model = Post
        fields = ['id', 'username', 'caption', 'media', 'uploaded_at']
        read_only_fields = ['id', 'username', 'uploaded_at']

    def validate_file(self, value):
        allowed_types = [
            'image/jpeg', 'image/png', 'image/gif', 
            'video/mp4', 'video/avi', 'video/mov',
        ]

        if value.content_type not in allowed_types:
            raise ValidationError("Unsupported file type")
        
        return value

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()

    def get_username(self, obj):
        return User.objects.get(id=obj.user_id.id).username
    
    class Meta:
        model = Like
        fields = ['id', 'post_id', 'username', 'like', 'total_likes', 'liked_at']
        read_only_fields = ['id', 'username', 'liked_at']

    def validate(self, data):
        user = self.context['request'].user
        data['user_id'] = user
        return data

    def get_total_likes(self, obj):
        return Like.objects.filter(post_id=obj.post_id, like=True).count()           