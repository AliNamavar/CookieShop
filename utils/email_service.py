from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    try:
        html_message = render_to_string(template_name, context)
        palined_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, palined_message, from_email, [to], html_message=html_message)

    except Exception as e:
        print(f"Error sending email: {e}")
