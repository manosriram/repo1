# Generated by Django 2.0 on 2018-06-16 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='post_image_model',
        ),
        migrations.DeleteModel(
            name='post_text_model',
        ),
    ]
