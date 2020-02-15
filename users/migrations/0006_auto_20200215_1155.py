# Generated by Django 2.2.5 on 2020-02-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_usercolorsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercolorsettings',
            name='color',
            field=models.BooleanField(choices=[('white', 'white'), ('blue', 'blue'), ('brown', 'brown'), ('dark-blue', 'dark-blue'), ('dark-brown', 'dark-brown'), ('dark-green', 'dark-green'), ('dark-grey', 'dark-grey'), ('dark-maroon', 'dark-maroon'), ('dark-pink', 'dark-pink'), ('dark-purple', 'dark-purple'), ('grey', 'grey'), ('orange', 'orange'), ('purple', 'purple'), ('red', 'red'), ('skyblue', 'skyblue'), ('teal', 'teal')], default='white', max_length=20, verbose_name='Цвет'),
        ),
    ]
