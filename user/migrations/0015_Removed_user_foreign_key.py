# Generated by Django 3.2.11 on 2022-03-09 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20220309_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='user',
        ),
    ]
