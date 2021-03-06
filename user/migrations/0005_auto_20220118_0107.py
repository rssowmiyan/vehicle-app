# Generated by Django 3.2.11 on 2022-01-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220118_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_of_registration',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
