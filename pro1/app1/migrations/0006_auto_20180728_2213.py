# Generated by Django 2.0 on 2018-07-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote_model',
            name='entrep',
            field=models.CharField(max_length=15),
        ),
    ]
