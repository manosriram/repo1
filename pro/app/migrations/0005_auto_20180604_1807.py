# Generated by Django 2.0 on 2018-06-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comments_feed_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_feed',
            name='comment',
            field=models.CharField(default='First one!', max_length=264),
        ),
    ]