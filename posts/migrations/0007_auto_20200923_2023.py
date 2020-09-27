# Generated by Django 2.2.16 on 2020-09-23 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200920_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_community', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]
