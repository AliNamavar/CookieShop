from numbers import Number

from django.shortcuts import render
from django.template.defaultfilters import title
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.http import Http404

from favorite_module.models import Favorite, FavoriteDetail
from product_module.models import Product, productCategory, ProductVisit, Product_Gallery
from django.db.models import Q
from utils.http_service import get_client_ip
from django.db.models import Q


# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    paginate_by = 1
    context_object_name = 'products'

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        query = query.filter(is_active=True)

        search_query = self.request.GET.get('search', None)
        if search_query:
            query = query.filter(Q(title__icontains=search_query))

        category_url = self.request.GET.get('category')
        if category_url:
            query = query.filter(category__url__iexact=category_url)

        return query

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categorise'] = productCategory.objects.filter(is_active=True).all()
        context['search_query'] = self.request.GET.get('search', '')
        context['product_count'] = Product.objects.all().count()

        return context


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        super(ProductDetailView, self).get_queryset()
        queryset = Product.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        products = self.object
        product_gallery = list(Product_Gallery.objects.filter(product_id=products.id).all())
        product_gallery.insert(0, products)
        context['product_gallery'] = product_gallery
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has__been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=products.id).exists()
        if not has__been_visited:
            new_visit = ProductVisit(
                ip=user_ip,
                user_id=user_id,
                product_id=products.id,
            )
            new_visit.save()
        related_products = Product.objects.filter(is_active=True, category__in=products.category.all()).exclude(
            id=products.id).distinct()[:12]
        context['related_products'] = related_products

        if self.request.user.is_authenticated:
            user_favorites = FavoriteDetail.objects.filter(
                favorite__user=self.request.user
            ).values_list('product_id', flat=True)
            context['user_favorites'] = user_favorites
        else:
            context['user_favorites'] = []


        return context
