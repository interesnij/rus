# Generated by Django 3.2 on 2021-06-14 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20210613_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soundlist',
            options={'verbose_name': 'плейлист', 'verbose_name_plural': 'плейлисты'},
        ),
        migrations.RemoveField(
            model_name='soundlist',
            name='order',
        ),
    ]