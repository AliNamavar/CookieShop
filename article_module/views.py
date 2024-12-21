from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.


class ArticleListView(ListView):
    model = ''
    template_name = 'article_module/article_list.html'