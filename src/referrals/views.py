from rest_framework import generics, permissions, viewsets, mixins

from referrals.models import Profile
from referrals.serializers import ProfileSerializer


class ProfileView(generics.RetrieveAPIView, generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    http_method_names = ["get", "put"]

    def get_queryset(self):
        user = self.request.user
        qs = Profile.objects.filter(user=user).select_related("user", "referrer").prefetch_related("referrals__user")

        return qs

    def get_object(self):
        queryset = self.get_queryset()
        profile = generics.get_object_or_404(queryset)

        return profile
