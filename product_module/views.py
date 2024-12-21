from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from product_module.models import Product


# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    paginate_by = 8
    context_object_name = 'products'

    def get_queryset(self):
        super(ProductListView, self).get_queryset()
        queryset = Product.objects.filter(is_active=True)
        return queryset



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'


    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        super(ProductDetailView, self).get_queryset()
        queryset = Product.objects.filter(is_active=True)
        return queryset
