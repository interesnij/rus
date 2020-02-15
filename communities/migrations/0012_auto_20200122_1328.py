# Generated by Django 2.2.5 on 2020-01-22 13:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0011_auto_20200121_1709'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='communitymembership',
            unique_together={('user', 'community')},
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user'], name='communities_communi_f9047f_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_administrator'], name='communities_communi_b6abad_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_moderator'], name='communities_communi_91a862_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_editor'], name='communities_communi_5976b6_idx'),
        ),
        migrations.AddIndex(
            model_name='communitymembership',
            index=models.Index(fields=['community', 'user', 'is_advertiser'], name='communities_communi_029e1f_idx'),
        ),
    ]
