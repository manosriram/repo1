# Generated by Django 2.0 on 2018-07-28 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_vote_model_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote_model',
            name='hits',
        ),
    ]