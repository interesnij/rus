# Generated by Django 2.2.5 on 2019-10-10 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0005_auto_20191010_1837'),
        ('main', '0005_auto_20191010_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='comments_enabled',
            field=models.BooleanField(default=True, verbose_name='Разрешить комментарии'),
        ),
        migrations.AddField(
            model_name='item',
            name='community',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communa', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together={('creator', 'community')},
        ),
    ]
