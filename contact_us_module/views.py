from django.shortcuts import render
from django.views.generic import TemplateView, View
from site_module.models import site_settings
from .forms import ContactForm
from .models import ContactUs
from django.template.loader import render_to_string
from django.http import HttpResponse
from utils.email_service import send_email
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your views here.
class ContactUsView(TemplateView):
    template_name = 'contact_us_module/contact_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        settings = site_settings.objects.filter(is_main_setting=True).first()
        work_hours = settings.work_hours.split('\n') if settings else []

        context = {
            'settings': settings,
            'work_hours': work_hours,
            'form': ContactForm()
        }

        return context


class ConfirmContactFormView(View):

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            newContact = ContactUs.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            newContact.save()

            response_html = render_to_string("contact_us_partials/success_article_comments.html", {
                "success_message": "نظر شما با موفقیت ثبت شد."
            }).strip()
            return HttpResponse(response_html)


@receiver(post_save, sender=ContactUs)
def send_reply_email(sender, instance, **kwargs):
    if instance.response:
        subject = "پاسخ به تیکت شما"
        to = instance.email
        context = {
            'ticket': instance.message,
            'name': instance.name,
            'response': instance.response,
        }

        print(instance.email)
        template_name = "send_mails/ticket_answer.html"
        send_email(subject, to, context, template_name)