from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('active-account', views.email_verification.as_view(), name='email_verification'),
    path('logput', views.logoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('forgot-password', views.ForgotPassView.as_view(), name='ForgotPassword'),
    path('forgot-password/<email_active_code>', views.ChangePass, name='ChangePass'),
]