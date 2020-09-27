# Generated by Django 2.2.16 on 2020-09-09 18:33

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import docs.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0002_auto_20200906_1514'),
        ('gallery', '0002_auto_20200906_1514'),
        ('goods', '0002_auto_20200906_1514'),
        ('posts', '0003_auto_20200908_1912'),
        ('docs', '0002_remove_doc_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('file', models.FileField(upload_to=docs.helpers.upload_to_doc_directory, verbose_name='Документ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('type', models.CharField(choices=[('P', 'Личный документ'), ('S', 'Учебный документ'), ('B', 'Книга'), ('O', 'Другой документ')], default='P', max_length=2)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('good_comment', models.ManyToManyField(blank=True, related_name='good_comment_doc', to='goods.GoodComment')),
                ('item', models.ManyToManyField(blank=True, related_name='item_doc', to='posts.Post')),
                ('item_comment', models.ManyToManyField(blank=True, related_name='comment_doc', to='posts.PostComment')),
                ('list', models.ManyToManyField(blank='True', related_name='doc_list', to='docs.DocList')),
                ('message', models.ManyToManyField(blank=True, related_name='message_doc', to='chat.Message')),
                ('photo_comment', models.ManyToManyField(blank=True, related_name='gallery_comment_doc', to='gallery.PhotoComment')),
                ('video_comment', models.ManyToManyField(blank=True, related_name='video_comment_doc', to='video.VideoComment')),
            ],
            options={
                'verbose_name_plural': 'Документы',
                'verbose_name': 'Документ',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
        migrations.AddIndex(
            model_name='doc2',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='docs_doc2_created_ae4874_brin'),
        ),
    ]
