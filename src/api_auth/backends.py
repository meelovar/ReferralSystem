from django.contrib.auth.backends import BaseBackend
from django.contrib import auth


class OtpBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, otp=None, **kwargs):
        if phone_number is None or otp is None:
            return

        try:
            user = self.__user_model_cls.objects.get_by_natural_key(phone_number)
        except self.__user_model_cls.DoesNotExist:
            return
        else:
            if user.check_otp(otp):
                return user

    def get_user(self, user_id):
        try:
            user = self.__user_model_cls.objects.get(pk=user_id)
        except self.__user_model_cls.DoesNotExist:
            return None

        return user

    __user_model_cls = auth.get_user_model()
