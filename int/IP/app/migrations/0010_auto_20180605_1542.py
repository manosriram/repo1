# Generated by Django 2.0 on 2018-06-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180605_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy_model',
            old_name='ph_no',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='buy_model',
            old_name='name_prod',
            new_name='product_name',
        ),
        migrations.AlterField(
            model_name='buy_model',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
