# Generated by Django 3.2 on 2023-06-06 06:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', ckeditor.fields.RichTextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('like', models.ManyToManyField(blank=True, related_name='product_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='5')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Customise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('sole', models.CharField(choices=[('platform', 'platform'), ('wedge heels', 'wedge heels')], max_length=150)),
                ('color', models.CharField(choices=[('beign', 'beign'), ('burgundy', 'burgundy'), ('red', 'red'), ('nude', 'nude')], max_length=150)),
                ('logo', models.BooleanField(default=False)),
                ('special_size', models.CharField(choices=[('UK 3', 'UK 3'), ('UK 3.5', 'UK 3.5'), ('UK 4', 'UK 4'), ('UK 4.5', 'UK 4.5'), ('UK 5', 'UK 5'), ('UK 5.5', 'UK 5.5'), ('UK 6', 'UK 6'), ('UK 6.5', 'UK 6.5'), ('UK 7', 'UK 7'), ('UK 7.5', 'UK 7.5'), ('UK 8', 'UK 8'), ('UK 8.5', 'UK 8.5'), ('UK 9', 'UK 9'), ('UK 9.5', 'UK 9.5')], max_length=150)),
                ('details', models.TextField(blank=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
