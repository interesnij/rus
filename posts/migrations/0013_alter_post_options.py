# Generated by Django 3.2 on 2021-06-14 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20210613_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-order'], 'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
    ]
