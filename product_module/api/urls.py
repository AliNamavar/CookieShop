from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductViewSet.as_view(), name='product-api-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]