# Generated by Django 4.1.7 on 2023-03-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='jewellery/pimg')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
