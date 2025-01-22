# Generated by Django 5.1.4 on 2024-12-21 23:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='عنوان')),
                ('url', models.CharField(max_length=150, verbose_name='عنوان (en) ')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(editable=False, max_length=400, unique=True, verbose_name=' عنوان (en)')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='images/article', verbose_name='تصویر')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد مقاله')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
