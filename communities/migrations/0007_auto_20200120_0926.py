# Generated by Django 2.2.5 on 2020-01-20 09:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0006_auto_20200119_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='starrers',
            field=models.ManyToManyField(blank=True, related_name='favorite_communities', to=settings.AUTH_USER_MODEL, verbose_name='Фавориты'),
        ),
    ]
