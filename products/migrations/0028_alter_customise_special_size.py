# Generated by Django 3.2 on 2023-06-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_customise_special_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customise',
            name='special_size',
            field=models.CharField(choices=[('UK 3', 'UK 3'), ('UK 3.5', 'UK 3.5'), ('UK 4', 'UK 4'), ('UK 4.5', 'UK 4.5'), ('UK 5', 'UK 5'), ('UK 5.5', 'UK 5.5'), ('UK 6', 'UK 6'), ('UK 6.5', 'UK 6.5'), ('UK 7', 'UK 7'), ('UK 7.5', 'UK 7.5'), ('UK 8', 'UK 8'), ('UK 8.5', 'UK 8.5'), ('UK 9', 'UK 9'), ('UK 9.5', 'UK 9.5')], max_length=150),
        ),
    ]
