# Generated by Django 3.0.8 on 2020-08-25 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_file',
        ),
    ]
