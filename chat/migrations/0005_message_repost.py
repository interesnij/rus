# Generated by Django 3.2 on 2021-06-26 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20210614_1807'),
        ('chat', '0004_rename_status_message_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='repost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_message', to='posts.post'),
        ),
    ]
