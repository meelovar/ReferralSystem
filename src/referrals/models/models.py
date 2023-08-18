from django.contrib import auth
from django.db import models

from referrals.services import generate_invite_code


class Profile(models.Model):
    user = models.OneToOneField(auth.get_user_model(), models.PROTECT, primary_key=True)
    invite_code = models.CharField(max_length=6, unique=True, default=generate_invite_code, editable=False)
    referrer = models.ForeignKey("self", models.PROTECT, related_name="referrals", null=True)
