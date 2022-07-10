# Generated by Django 3.2.7 on 2022-05-25 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20220525_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='movies',
        ),
        migrations.AddField(
            model_name='rating',
            name='movies',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='movies.movie'),
            preserve_default=False,
        ),
    ]