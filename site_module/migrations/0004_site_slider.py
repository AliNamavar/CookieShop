# Generated by Django 5.1.4 on 2024-12-16 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0003_alter_site_settings_work_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن پیام')),
                ('url', models.URLField(verbose_name='آدرس')),
                ('url_title', models.CharField(max_length=100, verbose_name='عنوان URL')),
                ('image', models.ImageField(upload_to='images/slider', verbose_name='عکس اسلایدر')),
            ],
            options={
                'verbose_name': 'site banner',
                'verbose_name_plural': "site banner's",
            },
        ),
    ]
