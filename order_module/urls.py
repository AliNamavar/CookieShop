from django.urls import path
from . import views
urlpatterns = [
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('cart-detail', views.cart_view, name='cart_detail'),
    path('remove-product-cart', views.remove_order_detail, name='remove_order_detail'),
    path('update-cart-product-count', views.update_cart_product_count, name='update_count_order_detail'),
    path('request-payment', views.request_payment, name='request_payment'),
    path('verify-payment', views.verify_payment, name='verify_payment'),
]