# Generated by Django 2.0 on 2018-07-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vote_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrep', models.CharField(choices=[('mark zuckerberg', 'Mark Zuckerberg'), ('steve jobs', 'Steve Jobs'), ('jack ma', 'Jack Ma'), ('elon musk', 'Elon Musk'), ('warren buffet', 'Warren Buffet')], default='Select Here.', max_length=15)),
            ],
        ),
    ]
