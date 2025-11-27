from django.urls import path
from .views import ChatRoomListCreateView, MessageListView, MessageCreateView

urlpatterns = [
    path('rooms/', ChatRoomListCreateView.as_view(), name='chatroom-list-create'),
    path('rooms/<int:room_id>/messages/', MessageListView.as_view(), name='message-list'),
    path('rooms/<int:room_id>/messages/new/', MessageCreateView.as_view(), name='message-create'),
]
