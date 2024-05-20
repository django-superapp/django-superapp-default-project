from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend
from django.db.models import Q


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.filter(Q(email=username) | Q(username=username)).first()
            if not user:
                return None
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

