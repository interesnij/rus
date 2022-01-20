# Generated by Django 3.2 on 2021-10-30 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0019_auto_20211030_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='music/artist/')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='MusicAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='music/artist/')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('count', models.PositiveIntegerField(default=0)),
                ('artist', models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist_playlist', to='music.artist', verbose_name='Исполнитель')),
                ('creator', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_playlist_album', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'плейлист',
                'verbose_name_plural': 'плейлисты',
            },
        ),
        migrations.RemoveField(
            model_name='soundtags',
            name='symbol',
        ),
        migrations.RemoveField(
            model_name='music',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='usertempmusiclist',
            name='tag',
        ),
        migrations.DeleteModel(
            name='SoundSymbol',
        ),
        migrations.DeleteModel(
            name='SoundTags',
        ),
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_playlist', to='music.musicalbum'),
        ),
    ]
