from django.urls import path
from .views import (
    LoginView,  
    ChangePasswordView,
    LogoutView,
    UserRegisterView,
)


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('change-password/', ChangePasswordView.as_view(), name='user-change-password'),
]
    