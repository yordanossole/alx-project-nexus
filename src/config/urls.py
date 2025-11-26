from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('auth/', include('custom_auth.urls')),
    # path('stories/', include('stories.urls')),
    # path('posts/', include('posts.urls')),
    # path('feed/', include('feed.urls')),
    
]
