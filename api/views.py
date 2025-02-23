from rest_framework.permissions import IsAdminUser
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class AdminSpectacularAPIView(SpectacularAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]


class AdminSpectacularSwaggerView(SpectacularSwaggerView):
    permission_classes = [IsAuthenticated, IsAdminUser]


class AdminSpectacularRedocView(SpectacularRedocView):
    permission_classes = [IsAuthenticated, IsAdminUser]
