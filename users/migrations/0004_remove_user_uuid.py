# Generated by Django 2.2.16 on 2020-09-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uuid',
        ),
    ]
