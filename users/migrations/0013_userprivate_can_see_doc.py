# Generated by Django 3.2 on 2021-07-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210721_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprivate',
            name='can_see_doc',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('M', 'Участники пространства или доски'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('FB', 'Друзья, кроме'), ('SF', 'Некоторые друзья'), ('MB', 'Участники, кроме'), ('SM', 'Некоторые участники')], default='AC', max_length=2, verbose_name='Кто видит документы'),
        ),
    ]
