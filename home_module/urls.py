from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us', views.AboutView.as_view(), name='about'),
    path("submit-feedback-form/", views.SubmitFeedbackView.as_view(), name="submit_feedback_form"),
    path("check-address/", views.check_address.as_view(), name="check_address"),

]