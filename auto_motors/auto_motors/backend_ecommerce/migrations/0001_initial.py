# Generated by Django 4.0.5 on 2022-06-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default=None, max_length=100)),
                ('desc', models.CharField(default=None, max_length=100)),
                ('preco', models.CharField(default=None, max_length=100)),
                ('status', models.CharField(default=None, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
