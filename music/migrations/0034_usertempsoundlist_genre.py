# Generated by Django 2.2.5 on 2020-01-17 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0033_auto_20200117_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertempsoundlist',
            name='genre',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre_field', to='music.SoundGenres', verbose_name='Связь на жанр'),
        ),
    ]
