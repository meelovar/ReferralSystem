from django.contrib import auth
from rest_framework import generics, status
from rest_framework.response import Response

from api_auth.serializers import UserVerifySerializer, UserOtpSerializer
from api_auth.services import send_otp


class OtpView(generics.CreateAPIView):
    serializer_class = UserOtpSerializer

    def post(self, request, *args, **kwargs):
        result = self.create(request, *args, **kwargs)

        send_otp()

        return result


class VerifyView(generics.CreateAPIView):
    serializer_class = UserVerifySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        headers = self.get_success_headers(serializer.data)

        auth.login(request, user)

        return Response(None, status.HTTP_202_ACCEPTED, headers=headers)
