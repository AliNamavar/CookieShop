from django.urls import path
from . import views
urlpatterns = [
    path('add-product-to-favorite', views.add_to_favorites.as_view(), name='add_to_favorites'),
]