from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import make_password

from api_auth.services import generate_otp


class UserManager(auth_models.BaseUserManager):
    def get_or_create_otp_user(self, phone_number):
        try:
            user = self.get_by_natural_key(phone_number)

            user.otp = generate_otp()

            user.save(update_fields=["otp"])
        except self.model.DoesNotExist:
            user = self.create_otp_user(phone_number)

        return user

    def create_otp_user(self, phone_number, **extra_fields):
        return self.__create_user(phone_number, None, generate_otp(), **extra_fields)

    def create_user(self, phone_number, password=None, **extra_field):
        return self.__create_user(phone_number, password, **extra_field)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.__create_user(phone_number, password, extra_fields)

    def __create_user(self, phone_number, password=None, otp=None, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)

        user.password = make_password(password)
        user.otp = otp

        user.save()

        return user
