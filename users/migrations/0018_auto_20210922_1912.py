# Generated by Django 3.2 on 2021-09-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210921_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprivate',
            name='can_add_in_chat',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто добавляет в беседы'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_community',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто видит сообщества'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_doc',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто видит документы'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_friend',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто видит друзей'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_good',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_info',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто видит информацию'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_music',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_photo',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_planner',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Участники пространства или доски'), ('F', 'Друзья'), ('FM', 'Друзья и участники'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья'), ('MB', 'Участники, кроме'), ('SM', 'Некоторые участники')], default='ME', max_length=2, verbose_name='Кто видит раздел планирования'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_post',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто видит стену'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_see_video',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AlterField(
            model_name='userprivate',
            name='can_send_message',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('AB', 'Друзья, кроме'), ('SF', 'Некоторые друзья')], default='AC', max_length=2, verbose_name='Кто пишет сообщения'),
        ),
    ]