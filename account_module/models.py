from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True, unique=False, verbose_name='نام کاربری')
    email = models.EmailField(unique=True, verbose_name='ایمیل')

    avatar = models.ImageField(upload_to='images/users', verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=75, verbose_name='کد فعالسازی ایمیل', null=True, blank=True)
    about_user = models.TextField(verbose_name='درباره کاربر', null=True, blank=True)
    address = models.CharField(max_length=250, verbose_name='آدرس کاربر')

    USERNAME_FIELD = 'email'  # شناسه ورود ایمیل
    REQUIRED_FIELDS = ['username']  # نام کاربری فیلد ضروری

    def __str__(self):
        return self.email
