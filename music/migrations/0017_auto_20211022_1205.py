# Generated by Django 3.2 on 2021-10-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20211014_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='is_track',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='soundlist',
            name='is_music_list',
            field=models.BooleanField(default=True),
        ),
    ]
