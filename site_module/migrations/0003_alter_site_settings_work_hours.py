# Generated by Django 5.1.4 on 2024-12-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_site_settings_work_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_settings',
            name='work_hours',
            field=models.TextField(verbose_name='ساعات کاری'),
        ),
    ]
