from rest_framework import serializers
from .models import Story, StoryViewed


class StorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Story
        fields = [
            'id', 'user', 'media', 'caption',
            'created_at', 'expires_at', 'is_highlighted'
        ]
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)


class StoryViewedSerializer(serializers.ModelSerializer):
    viewer = serializers.ReadOnlyField(source='viewer.id')

    class Meta:
        model = StoryViewed
        fields = ['id', 'story', 'viewer', 'viewed_at']
        read_only_fields = ['id', 'viewer', 'viewed_at']


