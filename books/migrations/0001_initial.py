# Generated by Django 5.0.4 on 2024-04-09 21:57

import books.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=50)),
                ('book_image', models.ImageField(blank=True, null=True, upload_to=books.models.image_method_book)),
                ('auther_image', models.ImageField(blank=True, null=True, upload_to=books.models.image_method_auther)),
                ('price', models.FloatField()),
                ('pages_number', models.IntegerField()),
                ('retal_price_day', models.FloatField(blank=True, null=True)),
                ('retal_period', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Available', 'Available'), ('Sold', 'Sold'), ('Rented', 'Rented')], default='Available', max_length=30, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
        ),
    ]
