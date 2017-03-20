from . models import student


class CustomUserAuth(object):
    def authenticate(self,username=None, password=None):
        try:
            user = student.objects.get(username=username)
            if user.check_password(password):
                return user
        except student.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            user = student.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except student.DoesNotExist:
            return None

