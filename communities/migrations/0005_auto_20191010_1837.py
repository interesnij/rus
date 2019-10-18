# Generated by Django 2.2.5 on 2019-10-10 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0004_auto_20191009_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityinvite',
            name='community',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AlterField(
            model_name='communityinvite',
            name='creator',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='created_communities_invites', to=settings.AUTH_USER_MODEL, verbose_name='Кто приглашает в сообщество'),
        ),
        migrations.AlterField(
            model_name='communityinvite',
            name='invited_user',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='communities_invites', to=settings.AUTH_USER_MODEL, verbose_name='Кого приглашают в сообщество'),
        ),
        migrations.AlterField(
            model_name='communitymembership',
            name='community',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AlterField(
            model_name='communitymembership',
            name='user',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='communities_memberships', to=settings.AUTH_USER_MODEL, verbose_name='Члены сообщества'),
        ),
        migrations.AlterUniqueTogether(
            name='communityinvite',
            unique_together={('invited_user', 'community', 'creator')},
        ),
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
    ]
