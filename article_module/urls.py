from django.urls import path
from . import views
urlpatterns = [
    path('article-list', views.ArticleListView.as_view(), name='article-list')
]