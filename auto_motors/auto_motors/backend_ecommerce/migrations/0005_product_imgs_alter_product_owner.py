# Generated by Django 4.0.5 on 2022-07-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_ecommerce', '0004_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imgs',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
