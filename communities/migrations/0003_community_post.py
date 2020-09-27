# Generated by Django 2.2.16 on 2020-09-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200912_1005'),
        ('communities', '0002_communitysectionsopen_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='post_community', to='posts.Post'),
        ),
    ]
