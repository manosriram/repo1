# Generated by Django 2.0 on 2018-06-06 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_register_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_model',
            name='repeat_Password',
        ),
    ]
