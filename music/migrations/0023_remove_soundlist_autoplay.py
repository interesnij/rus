# Generated by Django 2.2.5 on 2020-01-08 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0022_auto_20200107_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soundlist',
            name='autoplay',
        ),
    ]
