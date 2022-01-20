# Generated by Django 3.2 on 2021-12-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_delete_userprivate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileprivate',
            name='can_add_in_chat',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто добавляет в беседы'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_community',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто видит сообщества'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_doc',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто видит документы'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_friend',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто видит друзей'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_good',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_info',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто видит информацию'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_music',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_photo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_planner',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Участники пространства или доски'), (4, 'Друзья'), (3, 'Друзья и участники'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья'), (19, 'Участники, кроме'), (20, 'Некоторые участники')], default=2, verbose_name='Кто видит раздел планирования'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_post',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто видит стену'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_see_video',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='profileprivate',
            name='can_send_message',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (4, 'Друзья'), (5, 'Друзья и друзья друзей'), (6, 'Только я'), (17, 'Друзья, кроме'), (18, 'Некоторые друзья')], default=1, verbose_name='Кто пишет сообщения'),
        ),
    ]
