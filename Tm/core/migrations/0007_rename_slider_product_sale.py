# Generated by Django 4.0.6 on 2022-08-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_category_back_flip_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slider',
            new_name='sale',
        ),
    ]
