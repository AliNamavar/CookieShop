# Generated by Django 5.1.4 on 2024-12-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='site_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام سایت')),
                ('site_url', models.CharField(max_length=400, verbose_name='دامنه ی سایت')),
                ('about_text', models.TextField(verbose_name='درباره ی ما')),
                ('address', models.TextField(verbose_name='آدرست سایت')),
                ('phone_num', models.CharField(max_length=15, verbose_name='شماره ی تلفن')),
                ('email', models.CharField(max_length=150, verbose_name='ایمیل')),
                ('copy_right', models.TextField(verbose_name='کپی رایت')),
                ('site_logo', models.ImageField(upload_to='images/site_setting', verbose_name='لوگوی سایت')),
                ('is_main_setting', models.BooleanField(default=False, verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'site setting',
                'verbose_name_plural': "site Setting's",
            },
        ),
    ]
