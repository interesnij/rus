# Generated by Django 3.2 on 2021-05-29 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_music_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='status',
            new_name='type',
        ),
    ]