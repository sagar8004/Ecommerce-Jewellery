# Generated by Django 4.1.7 on 2023-03-23 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery', '0012_alter_product_desc_alter_product_meta_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='add_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_title',
        ),
    ]
