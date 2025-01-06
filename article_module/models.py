from django.db import models
from account_module.models import User
from django.utils.text import slugify


# Create your models here.

class ArticleCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=150, verbose_name='عنوان در url ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f'{self.title} - {self.url_title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', editable=False)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.CharField(max_length=150, verbose_name='عنوان در url ', unique=True, db_index=True)
    slug = models.SlugField(max_length=400, verbose_name=' عنوان (en)', unique=True, db_index=True, editable=False)
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/article', verbose_name='تصویر')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد مقاله')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    image_detail_one = models.ImageField(upload_to='images/article', verbose_name='تصویر برای جزییات مقاله', null=True, blank=True)
    image_detail_two = models.ImageField(upload_to='images/article', verbose_name='تصویر برای جزییات مقاله', null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.url_title)
        super().save(*args, **kwargs)


class article_comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده کامنت')
    comment = models.TextField(verbose_name='متن کامنت')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت کامنت')
    parent = models.ForeignKey('article_comments', on_delete=models.CASCADE, verbose_name='کامنت والد', null=True, blank=True)


    def __str__(self):
        return f'{self.article} - {self.user.username}'


    class Meta:
        verbose_name = 'Article_comment'
        verbose_name_plural = 'Article_comments'


class ArticleVisited(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    ip = models.CharField(max_length=30, verbose_name='ip  کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')


    def __str__(self):
        return f'{self.Article.title} - {self.ip}'

    class Meta:
        verbose_name = 'article_visit'
        verbose_name_plural = 'article_visits'