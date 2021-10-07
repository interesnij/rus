# Generated by Django 3.2 on 2021-07-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_goodcomment_sticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='type',
            field=models.CharField(choices=[('_PRO', 'Обработка'), ('_DRA', 'Черновик'), ('PUB', 'Опубликовано'), ('_DEL', 'Удалено'), ('_CLO', 'Закрыто модератором'), ('MAN', 'Созданный персоналом'), ('_DELM', 'Удалённый менеджерский'), ('_CLOM', 'Закрытый менеджерский')], default='_PRO', max_length=6, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='goodlist',
            name='type',
            field=models.CharField(choices=[('MAI', 'Основной'), ('LIS', 'Пользовательский'), ('MAN', 'Созданный персоналом'), ('_PRO', 'Обработка'), ('_DEL', 'Удалённый'), ('_DELM', 'Удалённый менеджерский'), ('_CLO', 'Закрытый менеджером'), ('_CLOM', 'Закрытый основной'), ('_CLOMA', 'Закрытый менеджерский')], default='_PRO', max_length=6, verbose_name='Тип альбома'),
        ),
    ]
