# Generated by Django 2.2.5 on 2020-01-05 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20200105_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('order', models.IntegerField(default=0)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.SoundSymbol', verbose_name='Буква')),
            ],
            options={
                'verbose_name_plural': 'треки тега',
                'verbose_name': 'треки тега',
            },
        ),
        migrations.AlterField(
            model_name='soundparsing',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.SoundTags', verbose_name='Буква'),
        ),
        migrations.DeleteModel(
            name='SoundTagsList',
        ),
    ]
