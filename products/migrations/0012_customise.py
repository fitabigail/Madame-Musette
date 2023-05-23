# Generated by Django 3.2 on 2023-05-22 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_is_customised'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customised_category', models.CharField(choices=[('sole', 'sole'), ('color', 'color'), ('logo', 'logo'), ('special_size', 'special_size')], max_length=150)),
                ('customised_value', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
