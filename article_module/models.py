from django.db import models
from account_module.models import User
from django.utils.text import slugify
# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='عنوان', db_index=True)
    url = models.CharField(max_length=150, verbose_name='عنوان (en) ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f'{self.name} - {self.url}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'





class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url = models.CharField(max_length=150, verbose_name='عنوان (en) ')
    slug = models.SlugField(max_length=400, verbose_name=' عنوان (en)', unique=True, db_index=True, editable=False)
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/article', verbose_name='تصویر')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد مقاله')
    is_active = models.BooleanField(default=False, verbose_name='فعال')

    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.url)
        super().save(*args, **kwargs)