from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class AuthToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    expires_at = models.DateTimeField()
    
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def __str__(self):
        return f"AuthToken(user={self.user}, token={self.token}, expires_at={self.expires_at})"

    def __repr__(self):
        return f"{self.user} at token {self.token}"
    
class SocialAccount(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)  # google, facebook
    uid = models.CharField(max_length=255)  # provider user id
    extra_data = models.JSONField(blank=True, null=True)
    
    def google_account(self):
        return self.provider.lower() == 'google'

    def facebook_account(self):
        return self.provider.lower() == 'facebook'
    
    def __repr__(self):
        return f"SocialAccount(user={self.user}, provider={self.provider}, uid={self.uid})"
    
    def __str__(self):
        return f"{self.user} - {self.provider} ({self.uid})"

class LoginAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    successful = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def detected_brute_force(self):
        if not self.successful and self.timestamp > timezone.now() - timedelta(minutes=5):
            attempts = LoginAttempt.objects.filter(
                ip_address = self.ip_address,
                successful = False,
                timestamp__gte = self.timestamp - timedelta(minutes=5)
            ).count()
            return attempts >= 5
        return False
    
    def __str__(self):
        return f"Login attempt by {self.user} at {self.timestamp} was {'successful' if self.successful else 'unsuccessful'}"

    def __repr__(self):
        return f"{self.user} login is {self.successful}"
    
class BlackListedToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    blacklisted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Blacklisted Token'
        verbose_name_plural = 'Blacklisted Tokens'
        
    def __str__(self):
        return f"BlacklistedToken(token={self.token}, blacklisted_at={self.blacklisted_at})"
    
    def __repr__(self):
        return f"BlacklistedToken(token={self.token})"
    
class PasswordResetToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    def is_expired(self):
        return timezone.now() > self.expires_at 
    
    def __str__(self):
        return f"PasswordResetToken(user={self.user}, token={self.token}, expires_at={self.expires_at})"
    
    def __repr__(self):
        return f"PasswordResetToken(user={self.user}, token={self.token})"