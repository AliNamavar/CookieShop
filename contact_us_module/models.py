from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    message = models.TextField(verbose_name='متن پیام')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال شده')
    response = models.TextField(verbose_name='جواب', blank=True, null=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='ادمین برسی کرد')


    def __str__(self):
        return f'{self.name} - {self.name}'

    class Meta:
        verbose_name = 'contact us'
        verbose_name_plural = 'contact us'