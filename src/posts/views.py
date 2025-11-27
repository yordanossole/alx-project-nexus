from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from custom_auth.permissions import IsRegularUser
from .serializer import PostSerializer
from .models import Posts


class PostAPIView(APIView):

    """
    API view to retrieve and create posts.

    Returns:
        Response: A response containing the list of posts or an error message.
  
    """

    permission_classes = [IsAuthenticated, IsRegularUser]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.filter(is_public=True).order_by('-created_at')
        serializer = self.serializer_class(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, 
            context={'request': request}
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.serializer_class(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        try:
            return Posts.objects.get(pk=self.kwargs['pk'])
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
