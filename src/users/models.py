from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
    BaseUserManager
)
from django.utils.translation import gettext_lazy as _

# def createUser(username, last_*args, **kwargs):

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        USER = 'user', 'User'
        GUEST = 'guest', 'Guest'
        
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(_("Phone number"), max_length=15, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['date_joined']
        
    def __str__(self):
        return f"{self.username} ({self.email}) - {self.get_role_display()}"
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.username
    
    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, role={self.get_role_display()})"

# class Group(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     members = models.ManyToManyField(User, through='GroupMember', related_name='groups')

#     class Meta:
#         verbose_name = 'Group'
#         verbose_name_plural = 'Groups'
#         ordering = ['name']

# class GroupMember(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_memberships')
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='members')
#     joined_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         unique_together = ('user', 'group')
#         verbose_name = 'Group Member'
#         verbose_name_plural = 'Group Members'
        
#     def __str__(self):
#         return f"{self.user.username} in {self.group.name}"
    
#     def __repr__(self):
#         return f"GroupMember(user={self.user.username}, group={self.group.name})"
# class UserProfile(models.Model):
#     username = models.CharField(unique=True, max_length=30)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     password = models.CharField(max_length=128)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
#     bio = models.TextField(blank=True, null=True)
#     avatar = models.ImageField(blank=True, null=True)

#     class Meta:
#         verbose_name = 'User Profile'
#         verbose_name_plural = 'User Profiles'

#     def __str__(self):
#         return f"{self.user.username}, {self.user.email}, {self.user.role}"

#     def __repr__(self):
#         return f"{self.user.username}, {self.user.email}, {self.user.role}"
    
#     def save(self, *args, **kwargs):
#         if not self.user.username:
#             self.user.username = self.user.email.split('@')[0]
#         super().save(*args, **kwargs)
        
#     def get_full_name(self):
#         return f"{self.user.first_name} {self.user.last_name}".strip()
    
