# Generated by Django 3.2 on 2021-10-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_auto_20211017_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_post',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='postslist',
            name='is_post_list',
            field=models.BooleanField(default=True),
        ),
    ]
