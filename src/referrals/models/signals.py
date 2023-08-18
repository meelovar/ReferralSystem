from django.contrib import auth
from django.dispatch import receiver

from referrals.models.models import Profile


@receiver(auth.user_logged_in)
def create_profile(user, **kwargs):
    if not hasattr(user, "profile"):
        Profile.objects.create(user=user)
