# Generated by Django 3.2 on 2023-05-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('1', 'Info'), ('2', 'Warranties'), ('3', 'Complaints')], default=1, max_length=100),
        ),
    ]