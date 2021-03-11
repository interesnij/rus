# Generated by Django 3.1.5 on 2021-03-11 13:38

import communities.helpers
from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('cover', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=communities.helpers.upload_to_community_avatar_directory)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('status', models.CharField(blank=True, max_length=100, verbose_name='статус-слоган')),
                ('type', models.CharField(choices=[('P', 'Публичное'), ('T', 'Приватное'), ('C', 'Закрытое')], default='P', max_length=2)),
                ('invites_enabled', models.BooleanField(default=True, verbose_name='Разрешить приглашения')),
                ('b_avatar', models.ImageField(blank=True, upload_to=communities.helpers.upload_to_community_cover_directory)),
                ('s_avatar', models.ImageField(blank=True, upload_to=communities.helpers.upload_to_community_cover_directory)),
                ('perm', models.CharField(choices=[('DE', 'Удален'), ('BL', 'Заблокирован'), ('CH', 'Детская'), ('ST', 'Обычные права'), ('VS', 'Запрос на проверку'), ('VE', 'Провернный')], default='ST', max_length=5, verbose_name='Уровень доступа')),
                ('have_link', models.CharField(blank=True, max_length=17, verbose_name='Ссылка')),
                ('banned_users', models.ManyToManyField(blank=True, related_name='banned_of_communities', to=settings.AUTH_USER_MODEL, verbose_name='Черный список')),
            ],
            options={
                'verbose_name': 'сообщество',
                'verbose_name_plural': 'сообщества',
            },
        ),
        migrations.CreateModel(
            name='CommunityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='Аватар')),
                ('order', models.IntegerField(default=0, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Категория сообществ',
                'verbose_name_plural': 'Категории сообществ',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CommunitySubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='Аватар')),
                ('order', models.IntegerField(default=0, verbose_name='Номер')),
                ('sudcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_categories', to='communities.communitycategory', verbose_name='Категория сообщества')),
            ],
            options={
                'verbose_name': 'Подкатегория сообществ',
                'verbose_name_plural': 'Подкатегории сообществ',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CommunitySectionsOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.BooleanField(default=True, verbose_name='Галерея открыта')),
                ('good', models.BooleanField(default=True, verbose_name='Товары открыты')),
                ('video', models.BooleanField(default=True, verbose_name='Видеоролики открыты')),
                ('music', models.BooleanField(default=True, verbose_name='Аудиозаписи открыты')),
                ('doc', models.BooleanField(default=True, verbose_name='Документы открыты')),
                ('link', models.BooleanField(default=True, verbose_name='Ссылки открыты')),
                ('article', models.BooleanField(default=True, verbose_name='Статьи открыты')),
                ('contacts', models.BooleanField(default=True, verbose_name='Контакты открыты')),
                ('discussion', models.BooleanField(default=True, verbose_name='Обсуждения открыты')),
                ('members', models.BooleanField(default=True, verbose_name='Подписчики открыты')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_sections_open', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPrivateVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(choices=[('VA', 'Ролики загружает персонал'), ('VM', 'Ролики загружают подписчики'), ('VNM', 'Ролики загружают все')], default='VA', max_length=5, verbose_name='Ролик')),
                ('comment', models.CharField(choices=[('CA', 'Комментарии пишет персонал'), ('CM', 'Комментарии пишут подписчики'), ('CNM', 'Комментарии пишут все')], default='CNM', max_length=5, verbose_name='Комментарии')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_private_video', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPrivatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wall', models.CharField(choices=[('SP', 'Персонал пишет'), ('SPMC', 'Персонал пишет, подписчики предлагают'), ('SPAC', 'Персонал пишет, все предлагают'), ('MP', 'Подписчики пишут'), ('MPAC', 'Подписчики пишут, все предлагают'), ('AC', 'На стене пишут все')], default='SP', max_length=5, verbose_name='Стена')),
                ('comment', models.CharField(choices=[('CA', 'Комментарии пишет персонал'), ('CM', 'Комментарии пишут подписчики'), ('CNM', 'Комментарии пишут все')], default='CNM', max_length=5, verbose_name='Комментарии')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_private_post', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPrivatePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(choices=[('PA', 'Фото загружает персонал'), ('PM', 'Фото загружают подписчики'), ('PNM', 'Фото загружают все')], default='PA', max_length=5, verbose_name='Фотографии')),
                ('comment', models.CharField(choices=[('CA', 'Комментарии пишет персонал'), ('CM', 'Комментарии пишут подписчики'), ('CNM', 'Комментарии пишут все')], default='CNM', max_length=5, verbose_name='Комментарии')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_private_photo', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPrivateMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.CharField(choices=[('VA', 'Аудиозаписи загружает персонал'), ('VM', 'Аудиозаписи загружают подписчики'), ('VNM', 'Аудиозаписи загружают все')], default='VA', max_length=5, verbose_name='Аудиозапись')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_private_music', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPrivateGood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.CharField(choices=[('GA', 'Товары загружает персонал'), ('GM', 'Товары загружают подписчики'), ('GNM', 'Товары загружают все')], default='GA', max_length=5, verbose_name='Товар')),
                ('comment', models.CharField(choices=[('CA', 'Комментарии пишет персонал'), ('CM', 'Комментарии пишут подписчики'), ('CNM', 'Комментарии пишут все')], default='CNM', max_length=5, verbose_name='Комментарии')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_private_good', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityNotificationsVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.BooleanField(default=True, verbose_name='Комментарий к ролику')),
                ('comment_reply', models.BooleanField(default=True, verbose_name='Ответ на комментарий к ролику')),
                ('repost', models.BooleanField(default=True, verbose_name='Репост ролика')),
                ('like', models.BooleanField(default=True, verbose_name='Лайк к ролику')),
                ('dislike', models.BooleanField(default=True, verbose_name='Дизлайк к ролику')),
                ('comment_like', models.BooleanField(default=True, verbose_name='Лайк на комментарий к ролику')),
                ('comment_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на комментарий к ролику')),
                ('comment_reply_like', models.BooleanField(default=True, verbose_name='Лайк на ответ к ролику')),
                ('comment_reply_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на ответ к ролику')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_notifications_video', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityNotificationsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.BooleanField(default=True, verbose_name='Комментарий к записи')),
                ('comment_reply', models.BooleanField(default=True, verbose_name='Ответ на комментарий к записи')),
                ('mention', models.BooleanField(default=True, verbose_name='Упоминание в записи')),
                ('comment_mention', models.BooleanField(default=True, verbose_name='Упоминание в комментарии к записи')),
                ('repost', models.BooleanField(default=True, verbose_name='Репост записи')),
                ('like', models.BooleanField(default=True, verbose_name='Лайк к записи')),
                ('dislike', models.BooleanField(default=True, verbose_name='Дизлайк к записи')),
                ('comment_like', models.BooleanField(default=True, verbose_name='Лайк на комментарий к записи')),
                ('comment_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на комментарий к записи')),
                ('comment_reply_like', models.BooleanField(default=True, verbose_name='Лайк на ответ к комментарию')),
                ('comment_reply_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на ответ к комментарию')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_notifications_post', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityNotificationsPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.BooleanField(default=True, verbose_name='Комментарий к фото')),
                ('comment_reply', models.BooleanField(default=True, verbose_name='Ответ на комментарий к фото')),
                ('repost', models.BooleanField(default=True, verbose_name='Репост фото')),
                ('like', models.BooleanField(default=True, verbose_name='Лайк к фото')),
                ('dislike', models.BooleanField(default=True, verbose_name='Дизлайк к фото')),
                ('comment_like', models.BooleanField(default=True, verbose_name='Лайк на комментарий к фото')),
                ('comment_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на комментарий к фото')),
                ('comment_reply_like', models.BooleanField(default=True, verbose_name='Лайк на ответ к фото')),
                ('comment_reply_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на ответ к фото')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_notifications_photo', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityNotificationsMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repost', models.BooleanField(default=True, verbose_name='Репост аудиозаписи')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_notifications_music', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityNotificationsGood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.BooleanField(default=True, verbose_name='Комментарий к товару')),
                ('comment_reply', models.BooleanField(default=True, verbose_name='Ответ на комментарий к товару')),
                ('repost', models.BooleanField(default=True, verbose_name='Репост товара')),
                ('like', models.BooleanField(default=True, verbose_name='Лайк к товару')),
                ('dislike', models.BooleanField(default=True, verbose_name='Дизлайк к товару')),
                ('comment_like', models.BooleanField(default=True, verbose_name='Лайк на комментарий к товару')),
                ('comment_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на комментарий к товару')),
                ('comment_reply_like', models.BooleanField(default=True, verbose_name='Лайк на ответ к товару')),
                ('comment_reply_dislike', models.BooleanField(default=True, verbose_name='Дизлайк на ответ к товару')),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_notifications_good', to='communities.community', verbose_name='Сообщество')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_administrator', models.BooleanField(default=False, verbose_name='Это администратор')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='Это модератор')),
                ('is_editor', models.BooleanField(default=False, verbose_name='Это редактор')),
                ('is_advertiser', models.BooleanField(default=False, verbose_name='Это рекламодатель')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('community', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='communities.community', verbose_name='Сообщество')),
                ('user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='communities_memberships', to=settings.AUTH_USER_MODEL, verbose_name='Члены сообщества')),
            ],
            options={
                'verbose_name': 'подписчик сообщества',
                'verbose_name_plural': 'подписчики сообщества',
            },
        ),
        migrations.CreateModel(
            name='CommunityLog',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('action_type', models.CharField(choices=[('B', 'Заблокировать'), ('U', 'Разблокировать'), ('AM', 'Добавить модератора'), ('RM', 'Удалить модератора'), ('AA', 'Добавить администратора'), ('RA', 'Удалить администратора'), ('OP', 'Открыть пост'), ('CP', 'Закрыть пост'), ('RP', 'Удалить пост'), ('RPC', 'Удалить комментарий к посту'), ('DPC', 'Отключить комментарии'), ('EPC', 'Включить комментарии')], editable=False, max_length=5)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='communities.community', verbose_name='Сообщество')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='posts.post', verbose_name='Пост')),
                ('source_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кто модерирует')),
                ('target_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кого модерируют')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='communities.community', verbose_name='Сообщество')),
                ('creator', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_communities_invites', to=settings.AUTH_USER_MODEL, verbose_name='Кто приглашает в сообщество')),
                ('invited_user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='communities_invites', to=settings.AUTH_USER_MODEL, verbose_name='Кого приглашают в сообщество')),
            ],
            options={
                'verbose_name': 'Приглашение в сообщество',
                'verbose_name_plural': 'Приглашения в сообщества',
            },
        ),
        migrations.AddField(
            model_name='community',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_sub_categories', to='communities.communitysubcategory', verbose_name='Подкатегория сообщества'),
        ),
        migrations.AddField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_communities', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user'], name='communities_communi_f9047f_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_administrator'], name='communities_communi_b6abad_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_moderator'], name='communities_communi_91a862_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_editor'], name='communities_communi_5976b6_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_advertiser'], name='communities_communi_029e1f_idx'),
        ),
        migrations.AddIndex(
            model_name='community',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='communities_created_2903f5_brin'),
        ),
    ]
