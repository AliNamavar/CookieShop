# Generated by Django 5.1.4 on 2024-12-21 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us_module', '0002_alter_contactus_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام'),
        ),
    ]
