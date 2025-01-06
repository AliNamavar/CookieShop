from django.urls import path
from . import views
urlpatterns = [
    path('products', views.ProductListView.as_view(), name='product-list'),
    path('products/cate/<str:category>', views.ProductListView.as_view(), name='product-categorise'),
    # path('products/search/<str:name>', views.ProductListView.as_view(), name='product-name-search'),

    path('products/<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]