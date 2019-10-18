# Generated by Django 2.2.5 on 2019-10-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userprofile_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sity',
            field=models.CharField(blank=True, max_length=64, verbose_name='Местоположение'),
        ),
    ]
