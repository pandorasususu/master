# Generated by Django 3.2.7 on 2022-05-23 05:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_remove_movie_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
