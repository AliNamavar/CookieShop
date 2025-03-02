# Generated by Django 5.1.4 on 2024-12-29 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_productcategory_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/productsgallery', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'product_gallery',
                'verbose_name_plural': 'product_gallery',
            },
        ),
    ]
