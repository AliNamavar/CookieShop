from rest_framework import generics, mixins
from .serializers import ProductSerializer
from product_module.models import Product
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .permissions import IsStaffUser

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]  # فقط کاربران staff که لاگین کردن

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]  # همینجا هم محدود شد
