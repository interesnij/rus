# Generated by Django 3.2 on 2021-09-27 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0015_auto_20210927_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videolist',
            old_name='can_see_item',
            new_name='can_see_el',
        ),
        migrations.RenameField(
            model_name='videolist',
            old_name='create_copy',
            new_name='copy_el',
        ),
        migrations.RenameField(
            model_name='videolist',
            old_name='create_item',
            new_name='create_el',
        ),
    ]
