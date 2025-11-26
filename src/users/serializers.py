from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import User

class UserSerializer(ModelSerializer):
    
    profile_picture_url = serializers.SerializerMethodField()
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
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
