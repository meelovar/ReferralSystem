from django.urls import path

from api_auth import views

urlpatterns = [
    path("otp/", views.OtpView.as_view(), name="api-auth-otp"),
    path("verify/", views.VerifyView.as_view(), name="api-auth-verify"),
]
