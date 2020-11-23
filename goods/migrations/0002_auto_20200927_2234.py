# Generated by Django 2.2.16 on 2020-09-27 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('video', '0001_initial'),
        ('chat', '0002_message_parent'),
        ('gallery', '0002_auto_20200927_2234'),
        ('communities', '0002_community_post'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='good_comment',
            field=models.ManyToManyField(blank=True, related_name='good_comment_good', to='goods.GoodComment'),
        ),
        migrations.AddField(
            model_name='good',
            name='item_comment',
            field=models.ManyToManyField(blank=True, related_name='comment_good', to='posts.PostComment'),
        ),
        migrations.AddField(
            model_name='good',
            name='message',
            field=models.ManyToManyField(blank=True, related_name='message_good', to='chat.Message'),
        ),
        migrations.AddField(
            model_name='good',
            name='photo_comment',
            field=models.ManyToManyField(blank=True, related_name='gallery_comment_good', to='gallery.PhotoComment'),
        ),
        migrations.AddField(
            model_name='good',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='item_good', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='good',
            name='video_comment',
            field=models.ManyToManyField(blank=True, related_name='video_comment_good', to='video.VideoComment'),
        ),
        migrations.AddField(
            model_name='goodalbum',
            name='community',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='good_album_community', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='goodalbum',
            name='message',
            field=models.ManyToManyField(blank=True, related_name='message_good_album', to='chat.Message'),
        ),
        migrations.AddField(
            model_name='goodalbum',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='post_good_album', to='posts.Post'),
        ),
    ]
