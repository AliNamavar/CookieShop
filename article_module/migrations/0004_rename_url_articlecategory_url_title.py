# Generated by Django 5.1.4 on 2024-12-22 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0003_alter_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecategory',
            old_name='url',
            new_name='url_title',
        ),
    ]
