# Generated by Django 2.0 on 2018-06-05 17:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180605_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='foot_com',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_foo', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='buy_model',
            name='phone_no',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999, 'Please Enter a Valid Phone Number')]),
        ),
    ]