# Generated by Django 3.2 on 2021-06-26 17:45

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_message_repost'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='chat',
            name='chat_chat_created_6a9d53_brin',
        ),
        migrations.AddIndex(
            model_name='chat',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='chat_chat_created_ab4521_brin'),
        ),
    ]
