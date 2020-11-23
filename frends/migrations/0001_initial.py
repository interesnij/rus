# Generated by Django 2.2.16 on 2020-09-27 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('target_connection', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='frends.Connect')),
                ('target_user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='targeted_connections', to=settings.AUTH_USER_MODEL, verbose_name='Кого переводит из подписчика в друзья')),
                ('user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to=settings.AUTH_USER_MODEL, verbose_name='Инициатор перевода из подписчика в друзья')),
            ],
            options={
                'verbose_name': 'Друг',
                'verbose_name_plural': 'Друзья',
                'unique_together': {('user', 'target_user')},
            },
        ),
    ]
