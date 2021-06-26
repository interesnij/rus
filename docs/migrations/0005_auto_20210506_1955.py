# Generated by Django 3.2 on 2021-05-06 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_alter_community_type'),
        ('docs', '0004_auto_20210505_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='is_community',
        ),
        migrations.AddField(
            model_name='doc',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_community', to='communities.community', verbose_name='Сообщество'),
        ),
    ]
