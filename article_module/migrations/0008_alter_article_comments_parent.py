# Generated by Django 5.1.4 on 2024-12-23 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0007_article_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.article_comments', verbose_name='کامنت والد'),
        ),
    ]
