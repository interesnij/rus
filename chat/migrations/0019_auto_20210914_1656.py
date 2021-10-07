# Generated by Django 3.2 on 2021-09-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0018_auto_20210914_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageversion',
            name='transfer',
        ),
        migrations.AddField(
            model_name='messageversion',
            name='transfer',
            field=models.ManyToManyField(blank=True, related_name='_chat_messageversion_transfer_+', to='chat.MessageVersion'),
        ),
    ]
