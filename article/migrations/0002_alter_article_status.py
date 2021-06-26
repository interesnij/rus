# Generated by Django 3.2 on 2021-04-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('_PRO', 'Обработка'), ('PUB', 'Опубликовано'), ('_DEL', 'Удалено'), ('PRI', 'Приватно'), ('_CLO', 'Закрыто модератором'), ('MAN', 'Созданный персоналом'), ('_DELP', 'Удалённый приватный'), ('_DELM', 'Удалённый менеджерский'), ('_CLOP', 'Закрытый приватный'), ('_CLOM', 'Закрытый менеджерский')], default='_PRO', max_length=5, verbose_name='Статус статьи'),
        ),
    ]
