# Generated by Django 3.2 on 2023-05-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20230522_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customise',
            old_name='customised_value_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='customise',
            old_name='customised_value_logo',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='customise',
            old_name='customised_value_sole',
            new_name='sole',
        ),
        migrations.RenameField(
            model_name='customise',
            old_name='customised_value_special_size',
            new_name='special_size',
        ),
    ]