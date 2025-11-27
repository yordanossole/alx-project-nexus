from rest_framework import serializers
from .models import ChatRoom, Message

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'sender_username', 'content', 'timestamp']
        read_only_fields = ['id', 'sender', 'timestamp', 'sender_username']

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']
