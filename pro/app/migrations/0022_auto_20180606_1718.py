# Generated by Django 2.0 on 2018-06-06 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20180606_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_model',
            name='saved',
        ),
        migrations.DeleteModel(
            name='register_model',
        ),
    ]
