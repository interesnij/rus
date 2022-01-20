# Generated by Django 3.2 on 2021-10-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_rename_status_article_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('PUB', 'Опубликовано'), ('_DEL', 'Удалено'), ('PRI', 'Приватно'), ('_CLO', 'Закрыто модератором'), ('MAN', 'Созданный персоналом'), ('_DELP', 'Удалённый приватный'), ('_DELM', 'Удалённый менеджерский'), ('_CLOP', 'Закрытый приватный'), ('_CLOM', 'Закрытый менеджерский')], max_length=5, verbose_name='Статус статьи'),
        ),
    ]
