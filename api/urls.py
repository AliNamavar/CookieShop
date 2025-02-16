from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # JSON schema
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('products/', include('product_module.api.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # دریافت Access و Refresh Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
