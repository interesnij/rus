# Generated by Django 3.2 on 2021-12-11 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0036_alter_chat_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Беседа', 'verbose_name_plural': 'Беседы'},
        ),
    ]
