from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    repeat_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'repeat_password']
        read_only_fields = ['id']

    def create(self, validated_data):
         validated_data.pop('repeat_password', None)
         password = validated_data.pop('password', None)
         user = User(**validated_data)
         if password:
             user.set_password(password)
         user.save()
         return user
    
    def validate(self, attrs):
            print(attrs)
            if attrs.get('password') == attrs.get('repeat_password'):
                return attrs
            raise serializers.ValidationError("Passwords do not match")

