# Generated by Django 5.1 on 2024-08-17 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0002_alter_product_category_alter_product_filter_brand_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderProduct',
        ),
    ]
