# Generated by Django 3.2 on 2021-12-13 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20211213_1928'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPrivate',
        ),
    ]
