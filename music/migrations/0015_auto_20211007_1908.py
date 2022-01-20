# Generated by Django 3.2 on 2021-10-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20210927_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundlist',
            name='can_see_el',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья'), (3, 'Друзья,друзья друзей'), (7, 'Только я'), (4, 'Друзья, кроме'), (5, 'Некоторые друзья'), (6, 'Подписчики'), (8, 'Администраторы'), (9, 'Подписчики, кроме'), (10, 'Некоторые подписчики')], default=1, verbose_name='Кто видит записи'),
        ),
        migrations.AlterField(
            model_name='soundlist',
            name='copy_el',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья'), (3, 'Друзья,друзья друзей'), (7, 'Только я'), (4, 'Друзья, кроме'), (5, 'Некоторые друзья'), (6, 'Подписчики'), (8, 'Администраторы'), (9, 'Подписчики, кроме'), (10, 'Некоторые подписчики')], default=1, verbose_name='Кто может копировать'),
        ),
        migrations.AlterField(
            model_name='soundlist',
            name='create_el',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Друзья'), (3, 'Друзья,друзья друзей'), (7, 'Только я'), (4, 'Друзья, кроме'), (5, 'Некоторые друзья'), (6, 'Подписчики'), (8, 'Администраторы'), (9, 'Подписчики, кроме'), (10, 'Некоторые подписчики')], default=7, verbose_name='Кто создает записи и потом с этими документами работает'),
        ),
    ]
