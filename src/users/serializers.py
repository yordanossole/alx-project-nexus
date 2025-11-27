from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import User, UserProfile

class UserSerializer(ModelSerializer):
    
    profile_picture_url = serializers.SerializerMethodField()
    phone_number = serializers.CharField(
        # source='profile.phone_number', 
        allow_blank=True, 
        required=False)
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name',
            'password',
            'profile_picture',
            'profile_picture_url',
            'phone_number',
            'is_verified',
            'created_at',
            'updated_at'
        ]
        
        read_only_fields = ['id', 'password', 'email', 'created_at', 'is_verified', 'picture_profile_url']  
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }
        
    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None
    
    def relational_fields(self):
        return {
            'user': serializers.PrimaryKeyRelatedField(read_only=True),
        }
        
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value
    
    def validate_phone_number(self, value):
        if value and User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number must be unique.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        # UserProfile.objects.create(
        #     user=user,
        #     bio=validated_data.get('bio', ''),
        #     profile_picture=validated_data.get('profile_picture'),
        #     phone_number=validated_data.get('phone_number', '')
        # )

        return user
