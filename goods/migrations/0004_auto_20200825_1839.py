# Generated by Django 3.1 on 2020-08-25 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
        ('gallery', '0004_auto_20200825_1839'),
        ('chat', '0001_initial'),
        ('video', '0003_auto_20200825_1828'),
        ('posts', '0003_remove_post_community'),
        ('goods', '0003_auto_20200825_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='good',
            name='good_comment',
            field=models.ManyToManyField(blank=True, related_name='good_comment_good', to='goods.GoodComment'),
        ),
        migrations.AddField(
            model_name='good',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='item_good', to='posts.Post'),
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
            name='video_comment',
            field=models.ManyToManyField(blank=True, related_name='video_comment_good', to='video.VideoComment'),
        ),
    ]
