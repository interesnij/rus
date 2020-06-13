# Generated by Django 2.2.5 on 2020-04-02 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0039_auto_20200402_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertempsoundlist',
            name='user',
            field=models.OneToOneField(db_index=False, default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_of_field', to=settings.AUTH_USER_MODEL, verbose_name='Слушатель'),
            preserve_default=False,
        ),
    ]
