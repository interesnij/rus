# Generated by Django 3.1.5 on 2021-03-11 13:35

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '__first__'),
        ('video', '__first__'),
        ('survey', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '__first__'),
        ('gallery', '__first__'),
        ('posts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'оставил комментарий к видеозаписи'), ('R', 'ответил на Ваш комментарий к видеозаписи'), ('PUM', 'упомянул Вас в видеозаписи'), ('PCUM', 'упомянул Вас в комментарии к видеозаписи'), ('L', 'оценил Вашу видеозапись'), ('D', 'не оценил Вашу видеозапись'), ('LC', 'оценил Ваш комментарий к видеозаписи'), ('DC', 'не оценил Ваш комментарий к видеозаписи'), ('LR', 'оценил Ваш ответ на комментарий к видеозаписи'), ('DR', 'не оценил Ваш ответ к комментарий к видеозаписи'), ('RE', 'поделился Вашей видеозаписью'), ('CR', 'поделилось Вашей видеозаписью'), ('ARE', 'поделился Вашим видеоальбомом'), ('ACR', 'поделилось Вашим видеоальбомом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.videoalbum')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.video')),
                ('video_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.videocomment')),
            ],
            options={
                'verbose_name': 'Уведомление - ролики пользователя',
                'verbose_name_plural': 'Уведомления - ролики пользователя',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='VideoCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'написал комментарий к видеозаписи'), ('R', 'ответил на комментарий к видеозаписи'), ('UM', 'упомянул сообщество в видеозаписи'), ('CUM', 'упомянул сообщество в комментарии к видеозаписи'), ('L', 'оценил видеозапись'), ('D', 'не оценил видеозапись'), ('LC', 'оценил комментарий к видеозаписи'), ('DC', 'не оценил комментарий к видеозаписи'), ('LR', 'оценил Ваш ответ на комментарий к видеозаписи'), ('DR', 'не оценил Ваш ответ к комментарий к видеозаписи'), ('RE', 'поделился видеозаписью'), ('CR', 'поделилось видеозаписью'), ('ARE', 'поделился фотоальбомом'), ('ACR', 'поделилось фотоальбомом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.videoalbum')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_community_notifications', to='communities.community', verbose_name='Сообщество')),
                ('community_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.video')),
                ('video_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.videocomment')),
            ],
            options={
                'verbose_name': 'Уведомление - ролики сообщества',
                'verbose_name_plural': 'Уведомления - ролики сообщества',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('CR', 'подал заявку в друзья'), ('CC', 'подтвердил, что он Ваш друг'), ('CI', 'пригласил Вас в сообщество')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Уведомление пользователя',
                'verbose_name_plural': 'Уведомления пользователя',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('verb', models.CharField(choices=[('CR', 'подал заявку в сообщество'), ('CC', 'принят в сообщество'), ('J', 'вступил в сообщество')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_users_notify', to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_user_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Уведомление сообщества',
                'verbose_name_plural': 'Уведомления сообщества',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SurveyNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('AV', 'Аноним принял участие в опросе'), ('V', ' принял участие в опросе'), ('RE', 'поделился Вашим опросом'), ('CR', 'поделилось Вашим опросом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
            options={
                'verbose_name': 'Уведомление - опросы пользователя',
                'verbose_name_plural': 'Уведомления - опросы пользователя',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SurveyCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('AV', 'Аноним принял участие в опросе'), ('V', ' принял участие в опросе'), ('RE', 'поделился Вашим опросом'), ('CR', 'поделилось Вашим опросом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('community_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_survey_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
            options={
                'verbose_name': 'Уведомление - опросы сообщества',
                'verbose_name_plural': 'Уведомления - опросы сообщества',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'оставил комментарий к записи'), ('R', 'ответил на Ваш комментарий к записи'), ('PUM', 'упомянул Вас в записи'), ('PCUM', 'упомянул Вас в комментарии к записи'), ('L', 'оценил Вашу запись'), ('D', 'не оценил Вашу запись'), ('LC', 'оценил Ваш комментарий к записи'), ('DC', 'не оценил Ваш комментарий к записи'), ('LR', 'оценил Ваш ответ на комментарий к записи'), ('DR', 'не оценил Ваш ответ к комментарий к записи'), ('RE', 'поделился Вашей записью'), ('CR', 'поделилось Вашей записью')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('object_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_post_object_set', to='notify.postnotify', verbose_name='Например, несколько человек лайкает пост. Нужно для группировки')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('post_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.postcomment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('user_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_post_user_set', to='notify.postnotify', verbose_name='Например, человек лайкает несколько постов. Нужно для группировки')),
            ],
            options={
                'verbose_name': 'Уведомление - записи пользователя',
                'verbose_name_plural': 'Уведомления - записи пользователя',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'написал комментарий к записи'), ('R', 'ответил на комментарий к записи'), ('UM', 'упомянул сообщество в записи'), ('CUM', 'упомянул сообщество в комментарии к записи'), ('L', 'оценил запись'), ('D', 'не оценил запись'), ('LC', 'оценил комментарий к записи'), ('DC', 'не оценил комментарий к записи'), ('LR', 'оценил Ваш ответ на комментарий к записи'), ('DR', 'не оценил Ваш ответ к комментарий к записи'), ('RE', 'поделился записью'), ('CR', 'поделилось записью')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_community_notifications', to='communities.community', verbose_name='Сообщество')),
                ('community_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('object_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='community_post_object_set', to='notify.postcommunitynotify', verbose_name='Например, несколько человек лайкает пост. Нужно для группировки')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('post_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.postcomment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_post_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('user_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='community_post_user_set', to='notify.postcommunitynotify', verbose_name='Например, человек лайкает несколько постов. Нужно для группировки')),
            ],
            options={
                'verbose_name': 'Уведомление - записи сообщества',
                'verbose_name_plural': 'Уведомления - записи сообщества',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PhotoNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'оставил комментарий к фото'), ('R', 'ответил на Ваш комментарий к фото'), ('UM', 'упомянул Вас в фото'), ('CUM', 'упомянул Вас в комментарии к фото'), ('L', 'оценил Ваше фото'), ('D', 'не оценил Ваше фото'), ('LC', 'оценил Ваш комментарий к фото'), ('DC', 'не оценил Ваш комментарий к фото'), ('LR', 'оценил Ваш ответ на комментарий к фото'), ('DR', 'не оценил Ваш ответ к комментарий к фото'), ('RE', 'поделился Вашей фотографией'), ('CR', 'поделилось Вашей фотографией'), ('ARE', 'поделился Вашим фотоальбомом'), ('ACR', 'поделилось Вашим фотоальбомом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.album')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.photo')),
                ('photo_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.photocomment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Уведомление - фотографии пользователя',
                'verbose_name_plural': 'Уведомления - фотографии пользователя',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PhotoCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'оставил комментарий к изображению сообщества'), ('R', 'ответил на комментарий к изображению сообщества'), ('L', 'понравилось изображение сообщества'), ('D', 'не понравилось изображение сообщества'), ('LC', 'понравился комментарий к изображению сообщества'), ('DC', 'не понравился комментарий к изображению сообщества'), ('LRC', 'понравился ответ на комментарий к изображению сообщества'), ('DRC', 'не понравился ответ к комментарий к изображению сообщества'), ('RE', 'поделился фотографией'), ('CR', 'поделилось фотографией'), ('ARE', 'поделился фотоальбомом'), ('ACR', 'поделилось фотоальбомом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.album')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_photo_notify', to='communities.community', verbose_name='Сообщество')),
                ('community_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.photo')),
                ('photo_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.photocomment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_photo_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Сообщество')),
            ],
            options={
                'verbose_name': 'Уведомление - фотографии сообщества',
                'verbose_name_plural': 'Уведомления - фотографии сообщества',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'оставил комментарий к товару'), ('R', 'ответил на Ваш комментарий к товару'), ('PUM', 'упомянул Вас в товаре'), ('PCUM', 'упомянул Вас в комментарии к товару'), ('L', 'оценил Вашу товар'), ('D', 'не оценил Вашу товар'), ('LC', 'оценил Ваш комментарий к товару'), ('DC', 'не оценил Ваш комментарий к товару'), ('LR', 'оценил Ваш ответ на комментарий к товару'), ('DR', 'не оценил Ваш ответ к комментарий к товару'), ('RE', 'поделился товаром'), ('CR', 'поделилось товаром'), ('ARE', 'поделился подборкой товаров'), ('ACR', 'поделилось подборкой товаров')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodalbum')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('good', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.good')),
                ('good_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodcomment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Уведомление - товары пользователя',
                'verbose_name_plural': 'Уведомления - товары пользователя',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('C', 'написал комментарий к товару'), ('R', 'ответил на комментарий к товару'), ('UM', 'упомянул сообщество в товаре'), ('CUM', 'упомянул сообщество в комментарии к товару'), ('L', 'оценил товар'), ('D', 'не оценил товар'), ('LC', 'оценил комментарий к товару'), ('DC', 'не оценил комментарий к товару'), ('LR', 'оценил Ваш ответ на комментарий к товару'), ('DR', 'не оценил Ваш ответ к комментарий к товару'), ('RE', 'поделился товаром'), ('CR', 'поделилось товаром'), ('ARE', 'поделился подборкой товаров'), ('ACR', 'поделилось подборкой товаров')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodalbum')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_good_notify', to='communities.community', verbose_name='Сообщество')),
                ('community_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('good', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.good')),
                ('good_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goodcomment')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_good_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Сообщество')),
            ],
            options={
                'verbose_name': 'Уведомление - товары сообщества',
                'verbose_name_plural': 'Уведомления - товары сообщества',
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='videonotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_vide_created_fcc923_brin'),
        ),
        migrations.AddIndex(
            model_name='videocommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_vide_created_5bfdc0_brin'),
        ),
        migrations.AddIndex(
            model_name='usernotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_user_created_66e4ae_brin'),
        ),
        migrations.AddIndex(
            model_name='usercommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_user_created_227a2e_brin'),
        ),
        migrations.AddIndex(
            model_name='surveynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_surv_created_07f05a_brin'),
        ),
        migrations.AddIndex(
            model_name='surveycommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_surv_created_04ad1f_brin'),
        ),
        migrations.AddIndex(
            model_name='postnotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_post_created_e59d59_brin'),
        ),
        migrations.AddIndex(
            model_name='postcommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_post_created_4bb373_brin'),
        ),
        migrations.AddIndex(
            model_name='photonotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_phot_created_261b99_brin'),
        ),
        migrations.AddIndex(
            model_name='photocommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_phot_created_a8f4fb_brin'),
        ),
        migrations.AddIndex(
            model_name='goodnotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_good_created_6e73f9_brin'),
        ),
        migrations.AddIndex(
            model_name='goodcommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_good_created_1be254_brin'),
        ),
    ]
