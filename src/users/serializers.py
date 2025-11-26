from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'password']
        read_only_fields = ['id']  
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }
    
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
        user = UserProfile(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
