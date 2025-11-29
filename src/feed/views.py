from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Feed
from .serializers import FeedSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FeedListView(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'post']

    @swagger_auto_schema(operation_summary='List feed items')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
