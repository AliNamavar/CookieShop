from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

from .views import ProductViewSet, ProductDetailView

# urlpatterns = [
#     path('', staff_member_required(views.ProductViewSet.as_view(), login_url='/login/'), name='product-api-list'),
#     path('<int:pk>/', staff_member_required(views.ProductDetailView.as_view(), login_url='login/'), name='product-detail'),
# ]
urlpatterns = [
    path('', ProductViewSet.as_view(), name='product-api-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
