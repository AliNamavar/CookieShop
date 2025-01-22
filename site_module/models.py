from django.db import models

# Create your models here.

class site_settings(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام سایت')
    site_url = models.CharField(max_length=400, verbose_name='دامنه ی سایت')
    about_text = models.TextField(verbose_name='درباره ی ما')
    address = models.TextField(verbose_name='آدرست سایت')
    phone_num = models.CharField(max_length=15, verbose_name='شماره ی تلفن')
    email = models.CharField(max_length=150, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='کپی رایت')
    site_logo = models.ImageField(upload_to='images/site_setting', verbose_name='لوگوی سایت')
    is_main_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی')
    work_hours = models.TextField(verbose_name='ساعات کاری')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')

    def __str__(self):
        return f'{self.name} - {self.site_url}'

    class Meta:
        verbose_name = 'site setting'
        verbose_name_plural = "site Setting's"


class site_slider(models.Model):
    text = models.TextField(verbose_name='متن پیام')
    url = models.URLField(verbose_name='آدرس')
    url_title = models.CharField(max_length=100, verbose_name='عنوان URL')
    image = models.ImageField(upload_to='images/slider', verbose_name='عکس اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')


    def __str__(self):
        return f'{self.text} - {self.url_title}'

    class Meta:
        verbose_name = 'site banner'
        verbose_name_plural = "site banner's"


# class ClientSay(models.Model):
#     text = models.TextField(verbose_name='')
#     author = models.ForeignKey
