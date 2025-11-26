import secrets
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from custom_auth.auth_jwt import CustomJWTAuthentication

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.permissions import AllowAny
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate

from . import serializers



class LoginView(APIView):
    
    # serializer_class = AuthTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.create_token(serializer.validated_data['user'])
        return Response(tokens, status=status.HTTP_200_OK)
    
    
# class RegistrationView(viewsets.ModelViewSet):
    
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(request.data.get('password'))
#             user.save()
#             return Response(UserProfileSerializer(user).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
       

# class SocialAccountView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [CustomJWTAuthentication]

#     def post(self, request, *args, **kwargs):
#         serializer = SocialAccountSerializer(data=request.data)

#         if serializer.is_valid():
#             social_account = serializer.save(user=request.user)
#             return Response(SocialAccountSerializer(social_account).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class LoginAttemptView(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     authentication_classes = [TokenAuthentication]

#     def create(self, request, *args, **kwargs):
#         serializer = LoginAttemptSerializer(data=request.data)

#         if serializer.is_valid():
#             login_attempt = serializer.save()
#             return Response(LoginAttemptSerializer(login_attempt).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class PasswordResetRequestView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = [TokenAuthentication]
    
#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             user = UserProfile.objects.get(email=email)
#             token = PasswordResetToken.objects.create(user=user)
#             # Here you would typically send the token to the user's email
#             return Response({'success': 'Password reset token sent'}, status=status.HTTP_200_OK)
#         except UserProfile.DoesNotExist:
#             return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
# class PasswordResetConfirmView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = [TokenAuthentication]
#     def post(self, request, uid, token):
#         try:
#             password_reset_token = PasswordResetToken.objects.get(uid=uid, token=token)
#             new_password = request.data.get('new_password')
#             if not new_password:
#                 return Response({'error': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)
            
#             if password_reset_token.is_expired():
#                 return Response({'error': 'Token has expired'}, status=status.HTTP_400_BAD_REQUEST)
#         except PasswordResetToken.DoesNotExist:
#             return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

#         # If we reach this point, the token is valid and not expired
#         user = password_reset_token.user
#         user.set_password(new_password)
#         user.save()
#         return Response({'success': 'Password has been reset'}, status=status.HTTP_200_OK)

# class PasswordResetView(APIView):
#     permission_classes = [AllowAny] 
#     authentication_classes = [TokenAuthentication]

#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

#         # Here you would typically trigger the password reset process
#         return Response({'success': 'Password reset link sent'}, status=status.HTTP_200_OK) 
    
# class LogoutView(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [CustomJWTAuthentication]  

#     def create(self, request, *args, **kwargs):
#         request.auth.delete()  # Assuming the token is stored in request.auth
#         return Response({'success': 'Logged out successfully'}, status=status.HTTP_200_OK)  
    
#     def __str__(self):
#         return f"LogoutView(user={self.request.user})"
    
#     def __repr__(self):
#         return f"LogoutView(user={self.request.user})"
    
    
# # class SocialLoginView(APIView):
# #     permission_classes = [AllowAny]
# #     authentication_classes = [CustomJWTAuthentication]
# #     def post(self, request):
# #         serializer = SocialAccountSerializer(data=request.data) 
# #         if serializer.is_valid():
# #             social_account = serializer.save(user=request.user)
# #             return Response(SocialAccountSerializer(social_account).data, status=status.HTTP_201_CREATED)

# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)