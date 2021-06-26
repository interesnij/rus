# Generated by Django 3.2 on 2021-06-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_rename_status_music_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='soundlist',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]