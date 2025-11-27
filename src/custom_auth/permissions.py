from rest_framework.permissions import BasePermission, SAFE_METHODS
    

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin()

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator()

class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_regular_user()

class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_guest()

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS