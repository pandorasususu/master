# Generated by Django 3.2.7 on 2022-05-23 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='like_users',
        ),
    ]
