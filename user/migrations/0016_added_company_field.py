# Generated by Django 3.2.11 on 2022-03-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_Removed_user_foreign_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='company',
            field=models.CharField(default='trimble', max_length=30),
        ),
    ]
