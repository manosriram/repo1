# Generated by Django 2.0 on 2018-06-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180605_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_model',
            name='address',
            field=models.TextField(max_length=264),
        ),
    ]
