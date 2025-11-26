from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get('username'), password=attrs.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        if not user.is_active:
            raise serializers.ValidationError("User account is inactive")
        attrs['user'] = user
        return attrs
    
    def create_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

# class AuthTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthToken
#         fields = ['user', 'token', 'expires_at']
#         read_only_fields = ['user', 'expires_at']
        
# class SocialAccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SocialAccount
#         fields = ['user', 'provider', 'uid', 'extra_data']
#         read_only_fields = ['user', 'provider', 'uid']
        
# class LoginAttemptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoginAttempt
#         fields = ['user', 'ip_address', 'successful', 'timestamp']
#         read_only_fields = ['user', 'timestamp']
        
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
        
#     # serializer_related_field = serializers.PrimaryKeyRelatedField

#     # def create(self, validated_data):
#     #     user = UserProfile(
#     #         username=validated_data['username'],
#     #         email=validated_data['email']
#     #     )
#     #     user.set_password(validated_data['password'])
#     #     user.save()
#     #     return user