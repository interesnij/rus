# Generated by Django 2.2.16 on 2020-09-06 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0001_initial'),
        ('follows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityfollow',
            name='community',
            field=models.ForeignKey(db_index=False, default='', on_delete=django.db.models.deletion.CASCADE, related_name='community', to='communities.Community', verbose_name='На какое сообщество подписывается'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='communityfollow',
            unique_together={('user', 'community')},
        ),
    ]
