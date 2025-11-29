from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MyProfileView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Get my profile",
        operation_description="Return the authenticated user's profile",
        responses={200: UserSerializer}
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class UserProfileView(APIView):
    
    @swagger_auto_schema(
        operation_summary="Get a user's profile",
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_PATH, description="Username", type=openapi.TYPE_STRING),
        ],
        responses={200: UserSerializer}
    )
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
class FollowUserView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Follow a user",
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_PATH, description="Username to follow", type=openapi.TYPE_STRING),
        ],
        responses={200: openapi.Response('Followed successfully')}
    )
    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)
        request.user.following.add(user_to_follow)
        return Response({ "message": f"You are now following {user_to_follow.username}"})
    
class UnFollowUserView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Unfollow a user",
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_PATH, description="Username to unfollow", type=openapi.TYPE_STRING),
        ],
        responses={200: openapi.Response('Unfollowed successfully')}
    )
    def post(self, request, username):
        user_to_unfollow = get_object_or_404(User, username=username)
        request.user.following.remove(user_to_unfollow)
        return Response({ "message": f"You have unfollowed {user_to_unfollow.username}"})
    
