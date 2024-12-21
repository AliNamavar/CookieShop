from django.urls import path
from . import views
urlpatterns = [
    path('contact-us', views.ContactUsView.as_view(), name='contact-us'),
    path('confirm-contact-form', views.ConfirmContactFormView.as_view(), name='submit-contact-form')
]