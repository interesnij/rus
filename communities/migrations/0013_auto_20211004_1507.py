# Generated by Django 3.2 on 2021-10-04 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0012_auto_20210921_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityPrivate',
            fields=[
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='community_private', serialize=False, to='communities.community', verbose_name='Сообщество')),
                ('can_see_member', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=3, verbose_name='Кто видит друзей')),
                ('can_see_community', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто видит сообщества')),
                ('can_see_info', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто видит информацию')),
                ('can_send_message', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто пишет сообщения')),
                ('can_see_post', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто видит стену')),
                ('can_see_photo', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто пишет сообщения')),
                ('can_see_good', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто пишет сообщения')),
                ('can_see_video', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто пишет сообщения')),
                ('can_see_music', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто пишет сообщения')),
                ('can_see_planner', models.CharField(choices=[(1, 'Все пользователи'), (2, 'Участники пространства или доски'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики'), (6, 'Участники, кроме'), (8, 'Некоторые участники')], default=2, max_length=2, verbose_name='Кто видит раздел планирования')),
                ('can_see_doc', models.CharField(choices=[(1, 'Все пользователи'), (3, 'Подписчики'), (4, 'Только я'), (5, 'Подписчики, кроме'), (7, 'Некоторые подписчики')], default=1, max_length=2, verbose_name='Кто видит документы')),
            ],
        ),
        migrations.RemoveField(
            model_name='communitymemberperm',
            name='can_add_in_chat',
        ),
        migrations.RemoveField(
            model_name='communitymemberperm',
            name='can_see_community',
        ),
        migrations.RemoveField(
            model_name='communitymemberperm',
            name='can_see_friend',
        ),
        migrations.AddField(
            model_name='communitymemberperm',
            name='can_see_members',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Не активно'), (1, 'Может иметь действия с элементом'), (2, 'Не может иметь действия с элементом')], default=0, verbose_name='Кто видит подписчиков'),
        ),
        migrations.AlterField(
            model_name='communitymemberperm',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_ie_settings', to='communities.communitymembership', verbose_name='Подписчик сообщества'),
        ),
        migrations.DeleteModel(
            name='CommunitySectionsOpen',
        ),
    ]
