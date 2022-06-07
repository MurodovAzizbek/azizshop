# Generated by Django 4.0.4 on 2022-04-21 16:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ProductColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='ProductSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'product tag',
                'verbose_name_plural': 'product tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('real_price', models.FloatField(default=0, verbose_name='real price')),
                ('discount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='discount')),
                ('short_description', models.TextField(verbose_name='short_description')),
                ('long_description', models.TextField(verbose_name='long_description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel', verbose_name='brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.categorymodel', verbose_name='category')),
                ('colors', models.ManyToManyField(related_name='products', to='products.productcolormodel')),
                ('izb', models.ManyToManyField(related_name='izb', to=settings.AUTH_USER_MODEL, verbose_name='wishlist')),
                ('sizes', models.ManyToManyField(related_name='products', to='products.productsizemodel')),
                ('tags', models.ManyToManyField(related_name='products', to='products.producttagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.productmodel', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product image',
                'verbose_name_plural': 'product images',
            },
        ),
    ]