# Generated by Django 3.2 on 2021-04-29 19:15

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов аудиозаписей'), ('DA', 'Удален создатель админов аудиозаписей'), ('CE', 'Добавлен создатель редакторов аудиозаписей'), ('DE', 'Удален создатель редакторов аудиозаписей'), ('CM', 'Добавлен создатель модераторов аудиозаписей'), ('DM', 'Удален создатель модераторов аудиозаписей')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера аудиозаписей',
                'verbose_name_plural': 'Логи создателей суперменеджеров аудиозаписей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AudioManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.PositiveIntegerField(default=0, verbose_name='Запись')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('R', 'Удален'), ('UR', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера аудиозаписей',
                'verbose_name_plural': 'Логи менеджеров аудиозаписей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AudioWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ аудиозаписей'), ('DA', 'Удален админ аудиозаписей'), ('CE', 'Добавлен редактор аудиозаписей'), ('DE', 'Удален редактор аудиозаписей'), ('CM', 'Добавлен модератор аудиозаписей'), ('DM', 'Удален модератор аудиозаписей')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера аудиозаписей',
                'verbose_name_plural': 'Логи супеменеджеров аудиозаписей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CommunityCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Сообщество')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов сообществ'), ('DA', 'Удален создатель админов сообществ'), ('CE', 'Добавлен создатель редакторов сообществ'), ('DE', 'Удален создатель редакторов сообществ'), ('CM', 'Добавлен создатель модераторов сообществ'), ('DM', 'Удален создатель модераторов сообществ'), ('CR', 'Добавлен создатель менеджеров рекламодателей сообществ'), ('DR', 'Удален создатель менеджеров рекламодателей сообществ')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера сообществ',
                'verbose_name_plural': 'Логи создателей суперменеджеров сообществ',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CommunityManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='Сообщество')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('D', 'Удалено'), ('UD', 'Восстановлено'), ('B', 'Заблокировано'), ('UB', 'Разблокировано'), ('C', 'Вечная заморозка'), ('H', 'Долгая заморозка'), ('M', 'Средняя заморозка'), ('L', 'Краткая заморозка'), ('US', 'Разморожено'), ('WB', 'Выставлен предупреждающий баннер'), ('NWB', 'Убран предупреждающий баннер'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера сообществ',
                'verbose_name_plural': 'Логи менеджеров сообществ',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CommunityWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Сообщество')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ сообществ'), ('DA', 'Удален админ сообществ'), ('CE', 'Добавлен редактор сообществ'), ('DE', 'Удален редактор сообществ'), ('CM', 'Добавлен модератор сообществ'), ('DM', 'Удален модератор сообществ'), ('CR', 'Добавлен менеджер рекламодателей сообществ'), ('DR', 'Удален менеджер рекламодателей сообществ')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера сообществ',
                'verbose_name_plural': 'Логи суперменеджеров сообществ',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodCommentManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.PositiveIntegerField(default=0, verbose_name='Комментарий к товару')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('R', 'Удален'), ('UR', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера комментария товаров',
                'verbose_name_plural': 'Логи комментариев менеджеров товаров',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов товаров'), ('DA', 'Удален создатель админов товаров'), ('CE', 'Добавлен создатель редакторов товаров'), ('DE', 'Удален создатель редакторов товаров'), ('CM', 'Добавлен создатель модераторов товаров'), ('DM', 'Удален создатель модераторов товаров')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера товаров',
                'verbose_name_plural': 'Логи создателей суперменеджеров товаров',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.PositiveIntegerField(default=0, verbose_name='Запись')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('R', 'Удален'), ('UR', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера товаров',
                'verbose_name_plural': 'Логи менеджеров товаров',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GoodWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ товаров'), ('DA', 'Удален админ товаров'), ('CE', 'Добавлен редактор товаров'), ('DE', 'Удален редактор товаров'), ('CM', 'Добавлен модератор товаров'), ('DM', 'Удален модератор товаров')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера товаров',
                'verbose_name_plural': 'Логи суперменеджеров товаров',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PhotoCommentManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.PositiveIntegerField(default=0, verbose_name='Комментарий к фотографии')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('R', 'Удален'), ('UR', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера комментария фотографии',
                'verbose_name_plural': 'Логи менеджеров комментарий фотографий',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PhotoCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов фотографий'), ('DA', 'Удален создатель админов фотографий'), ('CE', 'Добавлен создатель редакторов фотографий'), ('DE', 'Удален создатель редакторов фотографий'), ('CM', 'Добавлен создатель модераторов фотографий'), ('DM', 'Удален создатель модераторов фотографий')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера фотографий',
                'verbose_name_plural': 'Логи создателей суперменеджеров фотографий',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PhotoManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.PositiveIntegerField(default=0, verbose_name='Запись')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('R', 'Удален'), ('UR', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера фотографий',
                'verbose_name_plural': 'Логи менеджеров фотографий',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PhotoWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ фотографий'), ('DA', 'Удален админ фотографий'), ('CE', 'Добавлен редактор фотографий'), ('DE', 'Удален редактор фотографий'), ('CM', 'Добавлен модератор фотографий'), ('DM', 'Удален модератор фотографий')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера фотографий',
                'verbose_name_plural': 'Логи суперменеджеров фотографий',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostCommentManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.PositiveIntegerField(default=0, verbose_name='Комментарий к записи')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('D', 'Удален'), ('UD', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера комментария',
                'verbose_name_plural': 'Логи менеджеров комментариев',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов записей'), ('DA', 'Удален создатель админов записей'), ('CE', 'Добавлен создатель редакторов записей'), ('DE', 'Удален создатель редакторов записей'), ('CM', 'Добавлен создатель модераторов записей'), ('DM', 'Удален создатель модераторов записей')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера записей',
                'verbose_name_plural': 'Логи создателей суперменеджеров записей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.PositiveIntegerField(default=0, verbose_name='Запись')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('D', 'Удален'), ('UD', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера записи',
                'verbose_name_plural': 'Логи менеджеров записей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ записей'), ('DA', 'Удален админ записей'), ('CE', 'Добавлен редактор записей'), ('DE', 'Удален редактор записей'), ('CM', 'Добавлен модератор записей'), ('DM', 'Удален модератор записей')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера записей',
                'verbose_name_plural': 'Логи суперменеджеров записей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов пользователей'), ('DA', 'Удален создатель админов пользователей'), ('CE', 'Добавлен создатель редакторов пользователей'), ('DE', 'Удален создатель редакторов пользователей'), ('CM', 'Добавлен создатель модераторов пользователей'), ('DM', 'Удален создатель модераторов пользователей'), ('CR', 'Добавлен создатель менеджеров рекламодателей пользователей'), ('DR', 'Удален создатель менеджеров рекламодателей пользователей')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера пользоватетей',
                'verbose_name_plural': 'Логи создателей суперменеджеров пользоватетей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('D', 'Удален'), ('UD', 'Восстановлен'), ('B', 'Заблокирован'), ('UB', 'Разблокирован'), ('C', 'Вечная заморозка'), ('H', 'Долгая заморозка'), ('M', 'Средняя заморозка'), ('L', 'Краткая заморозка'), ('US', 'Разморожен'), ('WB', 'Выставлен предупреждающий баннер'), ('NWB', 'Убран предупреждающий баннер'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера пользоватетей',
                'verbose_name_plural': 'Логи менеджеров пользоватетей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ пользователей'), ('DA', 'Удален админ пользователей'), ('CE', 'Добавлен редактор пользователей'), ('DE', 'Удален редактор пользователей'), ('CM', 'Добавлен модератор пользователей'), ('DM', 'Удален модератор пользователей'), ('CR', 'Добавлен менеджер рекламодателей пользователей'), ('DR', 'Удален менеджер рекламодателей пользователей')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера пользоватетей',
                'verbose_name_plural': 'Логи суперменеджеров пользоватетей',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='VideoCommentManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.PositiveIntegerField(default=0, verbose_name='Комментарий к видеоролику')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('D', 'Удален'), ('UD', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='VideoCreateWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен создатель админов видеороликов'), ('DA', 'Удален создатель админов видеороликов'), ('CE', 'Добавлен создатель редакторов видеороликов'), ('DE', 'Удален создатель редакторов видеороликов'), ('CM', 'Добавлен создатель модераторов видеороликов'), ('DM', 'Удален создатель модераторов видеороликов')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог создателя суперменеджера видеороликов',
                'verbose_name_plural': 'Логи создателей суперменеджеров видеороликов',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='VideoManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.PositiveIntegerField(default=0, verbose_name='Запись')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('D', 'Удален'), ('UD', 'Восстановлен'), ('R', 'Жалоба отклонена'), ('UV', 'Проверка убрана')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог менеджера видеороликов',
                'verbose_name_plural': 'Логи менеджеров видеороликов',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='VideoWorkerManageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='Пользователь')),
                ('manager', models.PositiveIntegerField(default=0, verbose_name='Менеджер')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('action_type', models.CharField(choices=[('CA', 'Добавлен админ видеороликов'), ('DA', 'Удален админ видеороликов'), ('CE', 'Добавлен редактор видеороликов'), ('DE', 'Удален редактор видеороликов'), ('CM', 'Добавлен модератор видеороликов'), ('DM', 'Удален модератор видеороликов')], editable=False, max_length=5)),
            ],
            options={
                'verbose_name': 'Лог суперменеджера видеороликов',
                'verbose_name_plural': 'Логи суперменеджеров видеороликов',
                'ordering': ['-created'],
            },
        ),
        migrations.AddIndex(
            model_name='videoworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_videow_created_1e3689_brin'),
        ),
        migrations.AddIndex(
            model_name='videomanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_videom_created_42dd0b_brin'),
        ),
        migrations.AddIndex(
            model_name='videocreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_videoc_created_824c0d_brin'),
        ),
        migrations.AddIndex(
            model_name='userworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_userwo_created_884608_brin'),
        ),
        migrations.AddIndex(
            model_name='usermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_userma_created_b4d1bc_brin'),
        ),
        migrations.AddIndex(
            model_name='usercreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_usercr_created_8cde54_brin'),
        ),
        migrations.AddIndex(
            model_name='postworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_postwo_created_a340cf_brin'),
        ),
        migrations.AddIndex(
            model_name='postmanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_postma_created_8b04d5_brin'),
        ),
        migrations.AddIndex(
            model_name='postcreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_postcr_created_d5cdac_brin'),
        ),
        migrations.AddIndex(
            model_name='postcommentmanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_postco_created_ad3d5b_brin'),
        ),
        migrations.AddIndex(
            model_name='photoworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_photow_created_872f85_brin'),
        ),
        migrations.AddIndex(
            model_name='photomanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_photom_created_fd3694_brin'),
        ),
        migrations.AddIndex(
            model_name='photocreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_photoc_created_f47f50_brin'),
        ),
        migrations.AddIndex(
            model_name='photocommentmanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_photoc_created_0a6cc0_brin'),
        ),
        migrations.AddIndex(
            model_name='goodworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_goodwo_created_e54478_brin'),
        ),
        migrations.AddIndex(
            model_name='goodmanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_goodma_created_e0a0d2_brin'),
        ),
        migrations.AddIndex(
            model_name='goodcreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_goodcr_created_0fb5ab_brin'),
        ),
        migrations.AddIndex(
            model_name='goodcommentmanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_goodco_created_0af0ae_brin'),
        ),
        migrations.AddIndex(
            model_name='communityworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_commun_created_ac05c9_brin'),
        ),
        migrations.AddIndex(
            model_name='communitymanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_commun_created_8461e1_brin'),
        ),
        migrations.AddIndex(
            model_name='communitycreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_commun_created_94be02_brin'),
        ),
        migrations.AddIndex(
            model_name='audioworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_audiow_created_741078_brin'),
        ),
        migrations.AddIndex(
            model_name='audiomanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_audiom_created_2ca5ad_brin'),
        ),
        migrations.AddIndex(
            model_name='audiocreateworkermanagelog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='logs_audioc_created_a53a52_brin'),
        ),
    ]
