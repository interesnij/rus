# Generated by Django 2.2.16 on 2020-09-27 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('goods', '0001_initial'),
        ('gallery', '0001_initial'),
        ('video', '0001_initial'),
        ('communities', '0002_community_post'),
        ('chat', '0002_message_parent'),
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc2',
            name='good_comment',
            field=models.ManyToManyField(blank=True, related_name='good_comment_doc', to='goods.GoodComment'),
        ),
        migrations.AddField(
            model_name='doc2',
            name='item_comment',
            field=models.ManyToManyField(blank=True, related_name='comment_doc', to='posts.PostComment'),
        ),
        migrations.AddField(
            model_name='doc2',
            name='message',
            field=models.ManyToManyField(blank=True, related_name='message_doc', to='chat.Message'),
        ),
        migrations.AddField(
            model_name='doc2',
            name='photo_comment',
            field=models.ManyToManyField(blank=True, related_name='gallery_comment_doc', to='gallery.PhotoComment'),
        ),
        migrations.AddField(
            model_name='doc2',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='item_doc', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='doc2',
            name='video_comment',
            field=models.ManyToManyField(blank=True, related_name='video_comment_doc', to='video.VideoComment'),
        ),
        migrations.AddField(
            model_name='doclist',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_doclist', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='doclist',
            name='message',
            field=models.ManyToManyField(blank=True, related_name='message_doclist', to='chat.Message'),
        ),
        migrations.AddField(
            model_name='doclist',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='post_doclist', to='posts.Post'),
        ),
    ]
