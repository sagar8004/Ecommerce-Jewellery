# Generated by Django 4.1.7 on 2023-03-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery', '0004_alter_product_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
