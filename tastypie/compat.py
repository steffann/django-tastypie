from __future__ import unicode_literals
from django.conf import settings
import django

__all__ = ['get_user_model', 'get_username_field', 'AUTH_USER_MODEL']

# Get the user model from the settings, falling back to the pre-Django-1.5 default
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Django 1.5+ compatibility
if django.VERSION >= (1, 5):
    # Use the get_user_model method from Django
    from django.contrib.auth import get_user_model

    def get_username_field():
        # Get the username field from the model
        User = get_user_model()
        return User.USERNAME_FIELD

else:
    def get_user_model():
        # Return the pre-Django-1.5 User object
        from django.contrib.auth.models import User
        return User

    def get_username_field():
        # Get the pre-Django-1.5 default username
        return 'username'
