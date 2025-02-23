from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.decorators import login_required, user_passes_test
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('schema/', staff_member_required(SpectacularAPIView.as_view(), login_url='/login/'), name='schema'),
    path('swagger/', staff_member_required(SpectacularSwaggerView.as_view(url_name='schema'), login_url='/login/'), name='swagger-ui'),
    path('products/', include('product_module.api.urls'),name='product-api'),
    path('token/', staff_member_required(TokenObtainPairView.as_view(), login_url='/login/'), name='token_obtain_pair'),
    path('token/refresh/', staff_member_required(TokenRefreshView.as_view(), login_url='/login/'), name='token_refresh'),
]
