# Generated by Django 3.2.11 on 2022-01-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20220118_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_of_registration',
            field=models.DateField(),
        ),
    ]
