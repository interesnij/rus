# Generated by Django 3.2 on 2021-07-06 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20210706_1246'),
        ('chat', '0012_alter_message_unread'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sticker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='common.stickers'),
        ),
    ]
