# Generated by Django 3.2.8 on 2021-10-11 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_product__slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='_slug',
            new_name='slug',
        ),
    ]
