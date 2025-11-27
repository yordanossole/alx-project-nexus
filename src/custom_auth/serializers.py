from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        
        if not username and not email:
            return serializers.ValidationError("Either username or email must be provided.")
        
        
        user = authenticate(username=attrs.get('username'), email=attrs.get('email'), password=attrs.get('password'))
        
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
        
class UserRegisterSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password', 
            'password2', 
            'first_name', 
            'last_name',
            'profile_picture',
            'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'password2': {'write_only': True}
            }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        # UserProfile.objects.create (
        #     user=user,
        #     bio=validated_data.get('bio', ''),
        #     profile_picture=validated_data.get('profile_picture'),
        #     phone_number=validated_data.get('phone_number', '')
        # )
        
        return user
    


class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    def validate(self, attrs):
        user = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError("Old password is incorrect")
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

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