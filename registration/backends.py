from django.contrib.auth import backends
from registration.models import User

class EmailAuthBackend(backends.ModelBackend):

    def authenticate(self, request, username, password):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None
    def get_user(self,uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None