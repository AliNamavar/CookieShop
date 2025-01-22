from django.urls import path
from . import views
urlpatterns = [
    path('article-list', views.ArticleListView.as_view(), name='article-list'),
    path('article-cate/<str:category_url>/', views.ArticleListView.as_view(), name='article-category'),
    path('article-detail/<pk>/', views.ArticleDetailView.as_view(), name='article-Detail'),
    path('article-comment-post', views.ArticleDetailView.as_view(), name='article-comment')
]