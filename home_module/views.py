from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.db.models import Count

from account_module.models import User
from order_module.models import Order
from product_module.models import Product, productCategory
from site_module.models import site_settings, site_slider
from .forms import feedbackForm, check_address
from .models import feedback_Model, Gallery_Model
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.template.loader import render_to_string
from django.http import HttpResponse


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['settings']= site_settings.objects.filter(is_main_setting=True).first()
        context['sliders'] = site_slider.objects.filter(is_active=True)
        context['feedbacks'] = feedback_Model.objects.filter(satisfied=True).all().order_by('-created_date')
        context['form'] = feedbackForm()
        context['gallery'] = Gallery_Model.objects.filter(is_active=True).first()
        # context['products'] = Product.objects.filter(is_active=True, is_deleted=False).order_by('-id')[:8]
        context['products'] = Product.objects.filter(is_active=True, is_deleted=False).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[:8]
        context['categories'] = productCategory.objects.filter(is_active=True).all()

        return context






class SubmitFeedbackView(View):
    def post(self, request, *args, **kwargs):
        form = feedbackForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                return JsonResponse({
                    'status': 'not_auth',
                    'text': 'برای ارسال نظر باید وارد شوید',
                    'icon': 'info'
                })

            feedback = feedback_Model.objects.create(
                author=request.user,
                feedback=form.cleaned_data["text"],
                rating=form.cleaned_data["rating"],
                satisfied=True,
            )
            context = {
                'feedbacks': feedback_Model.objects.filter(satisfied=True).all().order_by('-created_date'),
            }
            return JsonResponse({
                'status': 'success',
                'text': 'نظر شما با موفقیت ثبت شد.',
                'icon': 'success',
                'body': render_to_string('partials/feedback_success.html', context)
            })

        print(form.errors)
        return JsonResponse({
            'status': 'error',
            'text': 'خطایی در ارسال نظر وجود دارد.',
            'icon': 'error',
        }, status=400)





class AboutView(TemplateView):
    template_name = 'home_module/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['settings'] = site_settings.objects.filter(is_main_setting=True).first()
        context['feedbacks'] = feedback_Model.objects.filter(satisfied=True).all().order_by('-created_date')
        return context


def header_component(request):
    if request.user.is_authenticated:
        cart, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(user=request.user,
                                                                                        is_paid=False)
        total_price = 0
        for product_detail in cart.orderdetail_set.all():
            total_price += product_detail.product.price * product_detail.count

    else:
        total_price = 0

    context = {
        'settings': site_settings.objects.filter(is_main_setting=True).first(),
        'total_price': total_price,

    }
    return render(request, 'shared/header_component.html', context)


def footer_component(request):
    settings = site_settings.objects.filter(is_main_setting=True).first()
    work_hours = settings.work_hours.split('\n') if settings else []
    context = {
        'settings': settings,
        'work_hours': work_hours
    }
    return render(request, 'shared/footer_component.html', context)





class check_address(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'home_module/adrees_check.html', context)

    def post(self, request, *args, **kwargs):
        new_address = request.POST.get('address')
        user_id = request.user.id
        user = User.objects.filter(id=user_id).first()
        user.address = new_address
        user.save()
        context = {
            'user': user
        }
        return render(request, 'home_module/adrees_check.html', context)
