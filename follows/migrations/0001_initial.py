# Generated by Django 3.1 on 2020-08-24 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityFollow',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('view', models.BooleanField(default=False, verbose_name='Просмотрено')),
                ('user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='community_follows', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик')),
            ],
            options={
                'verbose_name': 'Подписчик группы',
                'verbose_name_plural': 'Подписчики группы',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('view', models.BooleanField(default=False, verbose_name='Просмотрено')),
                ('followed_user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='На кого подписывается')),
                ('user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='follows', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
                'unique_together': {('user', 'followed_user')},
            },
        ),
    ]
