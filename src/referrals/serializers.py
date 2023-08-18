from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from referrals.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("phone_number", "invite_code", "referrer_code", "referrals")
        extra_kwargs = {
            "invite_code": {
                "read_only": True,
            },
            "referrals": {
                "read_only": True,
            },
        }

    phone_number = serializers.CharField(source="user.phone_number", read_only=True)
    referrer_code = serializers.CharField(source="referrer.invite_code", required=False)
    referrals = serializers.SerializerMethodField()

    @staticmethod
    def get_referrals(obj: Profile) -> list[str]:
        return [referral.user.phone_number for referral in obj.referrals.all()]

    def validate(self, attrs):
        referrer_code = attrs["referrer"]["invite_code"]

        if self.instance.referrer is not None:
            raise ValidationError({"referrer_code": "Can't change referrer code after it have been set"})

        try:
            referrer = self.Meta.model.objects.get(invite_code=referrer_code)
        except self.Meta.model.DoesNotExist:
            raise ValidationError({"referrer_code": "No profile with that invite code"})

        if referrer.user == self.instance.user:
            raise ValidationError({"referrer_code": "Referrer can't be set to self"})

        attrs["referrer"] = referrer

        return super().validate(attrs)
