# Generated by Django 4.1.7 on 2023-03-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery', '0011_product_add_info_product_desc_product_meta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(default='Descrpition here'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(default='Meta_titlt descrpition here', max_length=150),
        ),
    ]
