from django.contrib.auth import authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailorUsernameAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        if username:
            lookup = {'username' : username}
        elif email:
            lookup = {'email' : email}
        else:
            return
        
        try:
            user = UserModel.objects.get(**lookup)
        except UserModel.DoesNotExist:
            return

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None