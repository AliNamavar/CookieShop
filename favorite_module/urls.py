from django.urls import path
from . import views
urlpatterns = [
    path('add-product-to-favorite', views.add_to_favorites.as_view(), name='add_to_favorites'),
    path('Favorite-List', views.Favorite_View.as_view(), name='favorite_list'),
    path('Favorite-rm-product', views.remove_product_from_favorites.as_view(), name='favorite_remove'),
]