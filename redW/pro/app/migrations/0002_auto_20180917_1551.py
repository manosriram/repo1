# Generated by Django 2.0 on 2018-09-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(max_length=164),
        ),
    ]
