from rest_framework import serializers
from post.models import Post
from account.models import User
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user_id.username

    class Meta:
        model = Comment
        fields = ['id', 'post_id','username', 'content', 'total_comments', 'commented_at']
        read_only_fields = ['id', 'commented_at', 'username', 'total_comments']

    def validate(self, data):
        user = self.context['request'].user
        data['user_id'] = user
        return data
    
    def get_total_comments(self, obj):
        return Comment.objects.filter(post_id=obj.post_id).count()