from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    
)

registration_view = RegistrationView.as_view({
    'post': 'create'
})

logout_view = LogoutView.as_view({
    'post': 'logout'
})
# social_login_view = SocialLoginView.as_view({
#     'post': 'create'
# })


urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    # Password reset
    path('password-reset/request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset/confirm/<uid>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Social login (optional)
    # path('social-login/', SocialLoginView.as_view(), name='social_login'),
]
