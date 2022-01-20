# Generated by Django 3.2 on 2021-12-15 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0038_alter_chat_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='can_add_admin',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Все участники'), (2, 'Создатель'), (3, 'Создатель и админы'), (4, 'Участники кроме'), (5, 'Некоторые участники')], default=3, verbose_name='Кто назначает админов'),
        ),
        migrations.AlterField(
            model_name='message',
            name='copy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Копия', to='chat.message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('PUB', 'Опубликовано'), ('_DEL', 'Удалено'), ('EDI', 'Изменено'), ('_CLO', 'Закрыто модератором'), ('_DRA', 'Черновик'), ('_DELE', 'Удалённый измененный'), ('_CLOE', 'Закрытый измененный')], default='PUB', max_length=6, verbose_name='Статус сообщения'),
        ),
        migrations.CreateModel(
            name='MessageOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='Это сообщение пользователь удалил')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_options', to='chat.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_options_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь-инициатор исключения')),
            ],
        ),
    ]
