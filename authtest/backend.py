from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from authtest.models import User


def authenticate(username=None, password=None):
    user = User.objects.get(username=username)
    print(user)
    if user is not None:
        if user.check_password(password):
            return user
        else:
            return None

    return None


def get_user(self, user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None
