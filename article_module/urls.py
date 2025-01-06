from django.urls import path
from . import views
urlpatterns = [
    path('article-list', views.ArticleListView.as_view(), name='article-list'),
    path('article/<str:category_url>/', views.ArticleListView.as_view(), name='article-category'),
    path('<pk>/', views.ArticleDetailView.as_view(), name='article-Detail'),
    path('article-comment-post', views.ArticleDetailView.as_view(), name='article-comment')
]