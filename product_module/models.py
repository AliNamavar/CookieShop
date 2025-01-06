from django.db import models
from django.utils.text import slugify

from account_module.models import User


# Create your models here.

class productCategory(models.Model):
    ICON_CHOICES = [('flaticon-029-cupcake-3', 'Cupcake 3'), ('flaticon-034-chocolate-roll', 'Chocolate Roll'),
                    ('flaticon-005-pancake', 'Pancake'), ('flaticon-030-cupcake-2', 'Cupcake 2'),
                    ('flaticon-006-macarons', 'Macarons'), ]
    parent = models.ForeignKey('productCategory', on_delete=models.CASCADE, verbose_name='دست بندی والد', null=True,
                               blank=True)
    title = models.CharField(max_length=100, verbose_name='عنوان درسته بندی', db_index=True)
    url = models.CharField(max_length=100, verbose_name='عنوان در url', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف')
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='flaticon-006-macarons', verbose_name='آیکون', null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.url}'

    class Meta:
        verbose_name = 'products_category'
        verbose_name_plural = 'products_categorise'


class Product(models.Model):
    category = models.ManyToManyField(productCategory, verbose_name='دیته بندی')
    title = models.CharField(max_length=100, verbose_name='عنوان محصول', db_index=True)
    url_title = models.CharField(max_length=100, verbose_name='عنوان در url', db_index=True)
    price = models.IntegerField(verbose_name='قیمت محصول')
    image = models.ImageField(upload_to='images/products', verbose_name='تصویر اصلی')
    short_description = models.TextField(verbose_name='توضحات کوتاه محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    slug = models.SlugField(default="", db_index=True, unique=True, null=False, blank=True, max_length=400,
                            allow_unicode=True, verbose_name='slug')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف')
    number = models.IntegerField(verbose_name='حداقل مقدار خرید', default=1, blank=True, null=True)
    # created_date = models.DateTimeField(null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.url_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = "product's"


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='ip  کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')


    def __str__(self):
        return f'{self.product.title} - {self.ip}'

    class Meta:
        verbose_name = 'product_visit'
        verbose_name_plural = 'product_visits'

class Product_Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/productsgallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'product_gallery'
        verbose_name_plural = 'product_gallery'