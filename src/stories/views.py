from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Story, StoryViewed
from .serializers import StorySerializer, StoryViewedSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StoryListCreateView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'is_highlighted']

    @swagger_auto_schema(operation_summary='List stories')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Create story', request_body=StorySerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryViewedCreateView(generics.CreateAPIView):
    serializer_class = StoryViewedSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_summary='Mark story viewed', request_body=StoryViewedSerializer)
    def perform_create(self, serializer):
        serializer.save(viewer=self.request.user)

