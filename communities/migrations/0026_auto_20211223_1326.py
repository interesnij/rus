# Generated by Django 3.2 on 2021-12-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0025_alter_communitymembership_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityprivate2',
            name='can_see_log',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Подписчики'), (3, 'Создатель'), (5, 'Подписчики, кроме'), (6, 'Некоторые подписчики'), (4, 'Персонал')], default=3, verbose_name='Кто видит логи'),
        ),
        migrations.AddField(
            model_name='communityprivate2',
            name='can_see_settings',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все пользователи'), (2, 'Подписчики'), (3, 'Создатель'), (5, 'Подписчики, кроме'), (6, 'Некоторые подписчики'), (4, 'Персонал')], default=3, verbose_name='Кто видит настройки'),
        ),
    ]
