from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Posts, Comment, Like 

class PostSerializer(ModelSerializer):
    
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    def get_post_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

    def get_post_video_url(self, obj):
        if obj.video:
            return self.context['request'].build_absolute_uri(obj.video.url)
        return None
    

    class Meta:
        model = Posts
        fields = '__all__'
        
class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        
class LikeSerializer(ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'
        