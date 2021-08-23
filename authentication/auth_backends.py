from django.contrib.auth import get_user_model


User = get_user_model()


class PhoneAuthBackend(object):
    """
    Authenticate using phone number.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            if username.isnumeric():
                user = User.objects.get(phone_number=int(username))
                if user.check_password(password):
                    return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
