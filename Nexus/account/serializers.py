from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

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
    

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return {
            'refresh' : user.tokens()['refresh'],
            'access' : user.tokens()['access']
        }
    
    class Meta :
         model = User
         fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = auth.authenticate(email=email,password=password)
        if not user :
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active :
            raise AuthenticationFailed("Account disable")
        return {
            'email' : user.email,
            'tokens' : user.tokens
        }
    




