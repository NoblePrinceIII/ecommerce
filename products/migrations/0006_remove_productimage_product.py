# Generated by Django 3.0 on 2020-01-08 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
    ]
