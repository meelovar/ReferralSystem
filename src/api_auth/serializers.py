from django.contrib import auth
from rest_framework import serializers

from api_auth.models.validators import phone_validator


class UserAuthBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ("phone_number", "otp")
        extra_kwargs = {
            "otp": {
                "allow_null": False,
            }
        }

    phone_number = serializers.CharField(validators=[phone_validator])


class UserOtpSerializer(UserAuthBaseSerializer):
    class Meta(UserAuthBaseSerializer.Meta):
        extra_kwargs = {
            "otp": {
                "allow_null": False,
                "read_only": True,
            }
        }

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        user = self.Meta.model.objects.get_or_create_otp_user(phone_number)

        return user


class UserVerifySerializer(UserAuthBaseSerializer):
    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        otp = attrs.get("otp")
        user = auth.authenticate(self.context.get("request"), phone_number=phone_number, otp=otp)

        if not user:
            raise serializers.ValidationError("Wrong phone number or OTP", "authorization")

        attrs["user"] = user

        return super().validate(attrs)
