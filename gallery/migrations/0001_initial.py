# Generated by Django 2.2.16 on 2020-09-06 13:51

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import gallery.helpers
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='uuid')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_public', models.BooleanField(default=True, verbose_name='Виден другим')),
                ('type', models.CharField(choices=[('AV', 'Фото со страницы'), ('WA', 'Фото со стены'), ('MA', 'Основной альбом'), ('AL', 'Пользовательский альбом')], default='MA', max_length=5, verbose_name='Тип альбома')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_album_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Фотоальбом',
                'verbose_name_plural': 'Фотоальбомы',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='uuid')),
                ('file', imagekit.models.fields.ProcessedImageField(upload_to=gallery.helpers.upload_to_photo_directory)),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Описание')),
                ('is_public', models.BooleanField(default=True, verbose_name='Виден другим')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('comments_enabled', models.BooleanField(default=True, verbose_name='Разрешить комментарии')),
                ('votes_on', models.BooleanField(default=True, verbose_name='Реакции разрешены')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ManyToManyField(blank=True, related_name='photo_album', to='gallery.Album')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_edited', models.BooleanField(default=False, verbose_name='Изменено')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удаено')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Комментатор')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_comment_replies', to='gallery.PhotoComment', verbose_name='Родительский комментарий')),
                ('photo_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Photo')),
            ],
            options={
                'verbose_name': 'комментарий к записи',
                'verbose_name_plural': 'комментарии к записи',
            },
        ),
        migrations.AddIndex(
            model_name='photocomment',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='gallery_pho_created_7ebd02_brin'),
        ),
        migrations.AddIndex(
            model_name='photo',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='gallery_pho_created_389e41_brin'),
        ),
        migrations.AddIndex(
            model_name='album',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='gallery_alb_created_8f2540_brin'),
        ),
    ]
