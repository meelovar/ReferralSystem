from django.contrib.auth import models as auth_models
from django.db import models

from api_auth.models.validators import phone_validator
from api_auth.models.managers import UserManager


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    phone_number = models.CharField(validators=[phone_validator], unique=True)
    otp = models.CharField(max_length=4, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def check_otp(self, raw_otp: str) -> bool:
        is_correct = self.otp == raw_otp

        if is_correct:
            self.otp = None

            self.save(update_fields=["otp"])

        return is_correct
