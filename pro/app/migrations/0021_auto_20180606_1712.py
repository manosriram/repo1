# Generated by Django 2.0 on 2018-06-06 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_register_model_repeat_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_model',
            name='saved',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]