# Generated by Django 3.2 on 2021-04-30 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20210430_1519'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customlink',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_link', to='communities.community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='customlink',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_link', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
