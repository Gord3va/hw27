# Generated by Django 4.2.1 on 2023-05-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]