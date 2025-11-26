from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AuthToken, SocialAccount, LoginAttempt
from  users.models import UserProfile

UserProfile = get_user_model()

class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = ['user', 'token', 'expires_at']
        read_only_fields = ['user', 'expires_at']
        
class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ['user', 'provider', 'uid', 'extra_data']
        read_only_fields = ['user', 'provider', 'uid']
        
class LoginAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginAttempt
        fields = ['user', 'ip_address', 'successful', 'timestamp']
        read_only_fields = ['user', 'timestamp']
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    # serializer_related_field = serializers.PrimaryKeyRelatedField

    # def create(self, validated_data):
    #     user = UserProfile(
    #         username=validated_data['username'],
    #         email=validated_data['email']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user