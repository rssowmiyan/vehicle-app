# Generated by Django 3.2.11 on 2022-03-09 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0013_alter_vehicle_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='company',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
