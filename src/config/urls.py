from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('users.urls')),
    path('users/', include('users.urls')),  # optional plural alias
    path('auth/', include('custom_auth.urls')),
    path('posts/', include('posts.urls')),
    path('chats/', include('chat.urls')),
    path('stories/', include('stories.urls')),
    path('feed/', include('feed.urls')),

    # Swagger endpoints
    path('', RedirectView.as_view(url='swagger/', permanent=False)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
