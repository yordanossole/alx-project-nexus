from ast import Is
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User


class MyProfileView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class UserProfileView(APIView):
    
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
class FollowUserView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)
        request.user.following.add(user_to_follow)
        return Response({ "message": f"You are now following {user_to_follow.username}"})
    
class UnFollowUserView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, username):
        user_to_unfollow = get_object_or_404(User, username=username)
        request.user.following.remove(user_to_unfollow)
        return Response({ "message": f"You have unfollowed {user_to_unfollow.username}"})
    
