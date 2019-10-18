# Generated by Django 2.2.5 on 2019-10-10 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создан')),
                ('is_edited', models.BooleanField(default=False, verbose_name='Изменено')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Закрыто')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
        ),
    ]
