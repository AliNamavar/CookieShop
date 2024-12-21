from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from site_module.models import site_settings, site_slider
from .forms import feedbackForm
from .models import feedback_Model
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
        context = {
            'settings': site_settings.objects.filter(is_main_setting=True).first(),
            'sliders': site_slider.objects.filter(is_active=True),
            'feedbacks': feedback_Model.objects.filter(satisfied=True).all().order_by('-created_date'),
            'form': feedbackForm()

        }
        super(HomeView, self).get_context_data(**kwargs)

        return context


class SubmitFeedbackView(View):
    def post(self, request, *args, **kwargs):
        form = feedbackForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                response_html = render_to_string("partials/feedback_error.html", {
                    "error_message": "برای ارسال نظر باید ",
                })
                return HttpResponse(response_html)

            # ذخیره نظر
            feedback = feedback_Model.objects.create(
                author=request.user,
                feedback=form.cleaned_data["text"],
                rating=form.cleaned_data["rating"],
                satisfied=True,
            )

            response_html = render_to_string("partials/feedback_success.html", {
                "success_message": "نظر شما با موفقیت ثبت شد."
            }).strip()
            return HttpResponse(response_html)

        response_html = render_to_string("partials/feedback_error.html", {
            "form": form,
        })
        return JsonResponse({"html": response_html}, status=400)


class AboutView(TemplateView):
    template_name = 'home_module/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['settings'] = site_settings.objects.filter(is_main_setting=True).first()
        context['feedbacks'] = feedback_Model.objects.filter(satisfied=True).all().order_by('-created_date')
        return context


def header_component(request):
    context = {
        'settings': site_settings.objects.filter(is_main_setting=True).first()
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
