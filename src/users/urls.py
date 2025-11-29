from django.urls import path, re_path
from .views import MyProfileView, UserProfileView, FollowUserView, UnFollowUserView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="API for user management",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Your user API endpoints
    path("me/", MyProfileView.as_view(), name="my-profile"),
    path("<str:username>/", UserProfileView.as_view(), name="user-profile"),
    path("<str:username>/follow/", FollowUserView.as_view(), name="user_to_follow"),
    path("<str:username>/unfollow/", UnFollowUserView.as_view(), name="user_to_unfollow"),

    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # raw schema
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # redoc UI
]
