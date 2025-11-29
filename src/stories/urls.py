from django.urls import path
from .views import StoryListCreateView, StoryViewedCreateView

urlpatterns = [
    path('', StoryListCreateView.as_view(), name='story-list-create'),
    path('viewed/', StoryViewedCreateView.as_view(), name='story-viewed-create'),
]