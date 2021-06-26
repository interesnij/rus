# Generated by Django 3.2 on 2021-05-26 10:36

import communities.helpers
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_alter_community_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityinfo',
            name='b_avatar',
            field=models.ImageField(blank=True, upload_to=communities.helpers.upload_to_community_b_avatar_directory),
        ),
        migrations.AlterField(
            model_name='communityinfo',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=communities.helpers.upload_to_community_cover_directory),
        ),
    ]
