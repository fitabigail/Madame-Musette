# Generated by Django 3.2 on 2023-05-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_designer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_customized',
            field=models.BooleanField(default=False),
        ),
    ]