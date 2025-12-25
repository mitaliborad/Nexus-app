from rest_framework import serializers
from account.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.email.split('@')[0]

    class Meta:
        model = User
        fields = ['name', 'bio', 'profile_picture']
        read_only_fields = ['name'] 