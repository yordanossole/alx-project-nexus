from django.urls import path

from posts.views import PostAPIView, add_comment, like_post

urlpatterns = [
    path('', PostAPIView.as_view(), name='post-list'),
    path('<int:pk>/', PostAPIView.as_view(), name='post-detail'),
    path('<int:pk>/comments/', add_comment, name='post-add-comment'),
    path('<int:pk>/like/', like_post, name='post-like'),
]