# Generated by Django 5.1.4 on 2024-12-28 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0010_articlevisited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlevisited',
            old_name='product',
            new_name='Article',
        ),
    ]
