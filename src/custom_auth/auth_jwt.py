from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomJWTAuthentication(JWTAuthentication):
    
    def authenticate(self, request):
        row_token = self.get_raw_token(self.get_header(request))
        if row_token is None:
            return None
        
        validated_token = self.get_validated_token(row_token)
        user = self.get_user(validated_token)
        
        if not user.is_active:
            raise AuthenticationFailed('User is inactive', code='user_inactive')
        
        return (user, validated_token)