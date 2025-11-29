from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from config.pagination import DefaultPagination

from custom_auth.permissions import IsRegularUser
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Posts, Comment, Like
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PostAPIView(APIView):

    """
    API view to retrieve and create posts.

    Returns:
        Response: A response containing the list of posts or an error message.
  
    """

    permission_classes = [IsAuthenticated, IsRegularUser]
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_summary="List posts",
        responses={200: PostSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        posts = Posts.objects.filter(is_public=True).order_by('-created_at')
        paginator = DefaultPagination()
        page = paginator.paginate_queryset(posts, request)
        serializer = self.serializer_class(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create post",
        request_body=PostSerializer,
        responses={201: PostSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, 
            context={'request': request}
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary="Update post",
        request_body=PostSerializer,
        manual_parameters=[openapi.Parameter('pk', openapi.IN_PATH, type=openapi.TYPE_INTEGER)],
        responses={200: PostSerializer}
    )
    def put(self, request, *args, **kwargs):
        post = self._get_object_or_404()
        serializer = self.serializer_class(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Partial update post",
        request_body=PostSerializer,
        manual_parameters=[openapi.Parameter('pk', openapi.IN_PATH, type=openapi.TYPE_INTEGER)],
        responses={200: PostSerializer}
    )
    def patch(self, request, *args, **kwargs):
        post = self._get_object_or_404()
        serializer = self.serializer_class(
            post, data=request.data, partial=True, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete post",
        manual_parameters=[openapi.Parameter('pk', openapi.IN_PATH, type=openapi.TYPE_INTEGER)],
        responses={204: openapi.Response('Deleted')}
    )
    def delete(self, request, *args, **kwargs):
        post = self._get_object_or_404()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_object_or_404(self):
        return get_object_or_404(Posts, pk=self.kwargs['pk'])


@swagger_auto_schema(
    method='post',
    operation_summary='Add comment',
    manual_parameters=[openapi.Parameter('pk', openapi.IN_PATH, type=openapi.TYPE_INTEGER)],
    request_body=CommentSerializer,
    responses={201: CommentSerializer}
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    serializer = CommentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    operation_summary='Like post',
    manual_parameters=[openapi.Parameter('pk', openapi.IN_PATH, type=openapi.TYPE_INTEGER)],
    responses={201: LikeSerializer}
)
@swagger_auto_schema(
    method='delete',
    operation_summary='Unlike post',
    manual_parameters=[openapi.Parameter('pk', openapi.IN_PATH, type=openapi.TYPE_INTEGER)],
    responses={204: openapi.Response('Unliked')}
)
@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == 'POST':
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Already liked'}, status=status.HTTP_200_OK)
    else:
        Like.objects.filter(post=post, user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
