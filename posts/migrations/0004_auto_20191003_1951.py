# Generated by Django 2.2.5 on 2019-10-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20191002_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='object_id',
        ),
    ]
