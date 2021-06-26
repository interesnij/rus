# Generated by Django 3.2 on 2021-04-30 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20210430_1519'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videolist',
            name='communities',
            field=models.ManyToManyField(blank=True, related_name='_video_videolist_communities_+', to='communities.Community'),
        ),
        migrations.AddField(
            model_name='videolist',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_lists_community', to='communities.community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='videolist',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='_video_videolist_users_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
