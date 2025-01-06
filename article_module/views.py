from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.template.loader import render_to_string
from django.http import HttpResponse

from product_module.models import ProductVisit
from utils.http_service import get_client_ip
from .forms import CommentForm
from .models import Article, ArticleCategory, article_comments, ArticleVisited
from django.contrib.messages import get_messages


# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_module/article_list.html'
    paginate_by = 2
    ordering = ['created_date']
    context_object_name = 'Articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categorys'] = ArticleCategory.objects.filter(is_active=True).annotate(article_count=Count('article'))
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True).annotate(visit_count=Count('articlevisited')).order_by(
            '-visit_count')

        article_search = self.request.GET.get('article_search')
        if article_search is not None:
            query = query.filter(Q(title__icontains=article_search))

        category_url = self.kwargs.get('category_url')
        if category_url is not None:
            query = query.filter(category__url_title__iexact=category_url)

        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        article = self.object
        context['comments'] = (article_comments.objects.filter(parent_id=None, article_id=article.id).
                               prefetch_related('article_comments_set').order_by('-created_date'))
        context['form'] = CommentForm()
        context['comment_count'] = article_comments.objects.filter(article_id=article.id).count()

        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id


        has_been_visited = ArticleVisited.objects.filter(ip__iexact=user_ip, Article_id=article.id).exists()
        if not has_been_visited:
            new_visit = ArticleVisited(
                ip=user_ip,
                user_id=user_id,
                Article_id=article.id,
            )
            new_visit.save()

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            article_id = int(request.POST.get('articleid'))
            parent_id = request.POST.get('articleparentId')

            print(f"Article ID: {article_id}, Parent ID: {parent_id}")

            user = request.user
            parent_comment = article_comments.objects.get(id=parent_id) if parent_id else None
            article_comments.objects.create(
                user=user,
                article_id=article_id,
                comment=form.cleaned_data['message'],
                parent=parent_comment
            )

            response_html = render_to_string("article_partials/article_success.html", {
                "success_massage": "نظر شما با موفقیت ذخیره شد",
                'comments': (article_comments.objects.filter(parent_id=None, article_id=article_id).
                             prefetch_related('article_comments_set').order_by('-created_date')),
                # 'form': CommentForm(),
                'count': article_comments.objects.filter(article_id=article_id).count(),

            })

            return HttpResponse(response_html)
#test