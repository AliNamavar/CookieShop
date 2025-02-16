from rest_framework import generics, mixins
from .serializers import ProductSerializer
from product_module.models import Product
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
