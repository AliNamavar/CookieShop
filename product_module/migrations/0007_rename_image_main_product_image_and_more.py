# Generated by Django 5.1.4 on 2024-12-15 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_alter_product_image_four'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_main',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_four',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_sec',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_third',
        ),
    ]
