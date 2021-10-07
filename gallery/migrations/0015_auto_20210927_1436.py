# Generated by Django 3.2 on 2021-09-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20210911_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='photolist',
            name='can_see_comment',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья/подписчики'), (3, 'Друзья,друзья друзей/None'), (4, 'Только я/админы'), (5, 'Друзья/подписчики, кроме'), (6, 'Некоторые друзья/подписчики')], default=1, verbose_name='Кто видит комментарии'),
        ),
        migrations.AddField(
            model_name='photolist',
            name='can_see_item',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья/подписчики'), (3, 'Друзья,друзья друзей/None'), (4, 'Только я/админы'), (5, 'Друзья/подписчики, кроме'), (6, 'Некоторые друзья/подписчики')], default=1, verbose_name='Кто видит записи'),
        ),
        migrations.AddField(
            model_name='photolist',
            name='create_comment',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья/подписчики'), (3, 'Друзья,друзья друзей/None'), (4, 'Только я/админы'), (5, 'Друзья/подписчики, кроме'), (6, 'Некоторые друзья/подписчики')], default=1, verbose_name='Кто пишет комментарии'),
        ),
        migrations.AddField(
            model_name='photolist',
            name='create_copy',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья/подписчики'), (3, 'Друзья,друзья друзей/None'), (4, 'Только я/админы'), (5, 'Друзья/подписчики, кроме'), (6, 'Некоторые друзья/подписчики')], default=1, verbose_name='Кто может копировать'),
        ),
        migrations.AddField(
            model_name='photolist',
            name='create_item',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья/подписчики'), (3, 'Друзья,друзья друзей/None'), (4, 'Только я/админы'), (5, 'Друзья/подписчики, кроме'), (6, 'Некоторые друзья/подписчики')], default=4, verbose_name='Кто создает записи и потом с этими документами работает'),
        ),
    ]
