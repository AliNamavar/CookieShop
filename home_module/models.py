from django.db import models
from account_module.models import User
# Create your models here.

class feedback_Model(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    feedback = models.TextField(verbose_name='متن پیام')
    satisfied = models.BooleanField(verbose_name='کاربر راضی بوده؟')
    rating = models.PositiveIntegerField(default=1, verbose_name='امتیاز (1 تا 5)')


    def __str__(self):
        return f'{self.author} - {self.rating}'


    class Meta:
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'


