# Generated by Django 3.2.11 on 2022-01-17 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_vehicle_details_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='registration_number',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[('two_wheeler', 'Two wheeler'), ('four_wheeler', 'Four wheeler')], max_length=50),
        ),
    ]
