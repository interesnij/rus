# Generated by Django 2.2.16 on 2020-09-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200908_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Черновик'), ('PG', 'Обработка'), ('P', 'Опубликована'), ('MP', 'РЕпост в сообщения'), ('A', 'Архивирована'), ('C', 'Репост фотографии'), ('PAR', 'Репост фотоальбома'), ('GR', 'Репост товара'), ('MR', 'Репост аудиозаписи'), ('MLR', 'Репост плейлиста аудиозаписей'), ('DR', 'Репост документа'), ('DLR', 'Репост списка документов'), ('VR', 'Репост видеозаписи'), ('VLR', 'Репост списка видеозаписей'), ('UR', 'Репост пользователя'), ('CR', 'Репост сообщества')], default='P', max_length=5, verbose_name='Статус статьи'),
        ),
    ]
