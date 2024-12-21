from django.db import models
from django.utils.text import slugify


# Create your models here.

class productCategory(models.Model):
    parent = models.ForeignKey('productCategory', on_delete=models.CASCADE, verbose_name='دست بندی والد', null=True,
                               blank=True)
    title = models.CharField(max_length=100, verbose_name='عنوان درسته بندی', db_index=True)
    url = models.CharField(max_length=100, verbose_name='عنوان در url', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return f'{self.title} - {self.url}'

    class Meta:
        verbose_name = 'products_category'
        verbose_name_plural = 'products_categorise'


class Product(models.Model):
    category = models.ManyToManyField(productCategory, verbose_name='دیته بندی')
    title = models.CharField(max_length=100, verbose_name='عنوان محصول', db_index=True)
    price = models.IntegerField(verbose_name='قیمت محصول')
    image = models.ImageField(upload_to='images/products', verbose_name='تصویر اصلی')
    short_description = models.TextField(verbose_name='توضحات کوتاه محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    slug = models.SlugField(default="", db_index=True, unique=True, null=False, blank=True, max_length=400,
                            allow_unicode=True, verbose_name='slug')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = "product's"
