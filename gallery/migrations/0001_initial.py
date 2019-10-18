# Generated by Django 2.2.5 on 2019-10-18 14:03

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import gallery.helpers
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
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('order', models.PositiveIntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='uuid')),
                ('file', models.ImageField(upload_to=gallery.helpers.upload_to_photo_directory)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_public', models.BooleanField(default=True, verbose_name='Виден другим')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('order', models.PositiveIntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
            ],
            options={
                'ordering': ['order'],
            },
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
