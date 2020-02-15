# Generated by Django 2.2.5 on 2020-01-05 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_auto_20191223_1222'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0014_auto_20200105_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soundlist',
            options={'verbose_name': 'список: весь, человека или сообщества', 'verbose_name_plural': 'списки: весь, человека или сообщества'},
        ),
        migrations.AlterModelOptions(
            name='soundsymbol',
            options={'verbose_name': 'буква поиска музыки', 'verbose_name_plural': 'буквы поиска музыки'},
        ),
        migrations.AlterModelOptions(
            name='soundtags',
            options={'verbose_name': 'музыкальный тег', 'verbose_name_plural': 'музыкальные теги'},
        ),
        migrations.AddField(
            model_name='soundlist',
            name='community',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='soundlist',
            name='creator',
            field=models.ForeignKey(db_index=False, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SoundTagsList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('autoplay', models.BooleanField(default=False)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.SoundTags', verbose_name='Буква')),
                ('track', models.ManyToManyField(blank='True', to='music.SoundParsing')),
            ],
            options={
                'verbose_name': 'треки тега',
                'verbose_name_plural': 'треки тега',
            },
        ),
    ]
