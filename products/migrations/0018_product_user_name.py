# Generated by Django 3.2 on 2023-05-30 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0017_auto_20230529_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
