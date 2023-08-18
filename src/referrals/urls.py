from django.urls import path

from referrals import views

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
