# Generated by Django 5.1.4 on 2024-12-16 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_site_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_slider',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیر فعال'),
        ),
    ]
