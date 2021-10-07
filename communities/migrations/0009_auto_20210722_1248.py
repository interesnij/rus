# Generated by Django 3.2 on 2021-07-22 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210722_1248'),
        ('communities', '0008_auto_20210618_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityDocAddExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityDocAddIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityDocCanSeeExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityDocCanSeeIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodAddCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodAddCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodAddItemExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodAddItemIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodCanSeeCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodCanSeeCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodCanSeeMarketExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityGoodCanSeeMarketIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMembersCanSeeExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMembersCanSeeIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMessageCanSeeExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMessageCanSeeIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMusicAddItemExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMusicAddItemIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMusicCanSeeMusicExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMusicCanSeeMusicIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoAddCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoAddCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoAddItemExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoAddItemIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoCanSeeCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoCanSeeCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoCanSeeGalleryExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPhotoCanSeeGalleryIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeBoardsExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeBoardsIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeCardsExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeCardsIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeCommentsExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeCommentsIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeWorkspacesExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPlannerCanSeeWorkspacesIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostAddCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostAddCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostAddItemExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostAddItemIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostCanSeeCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostCanSeeCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostCanSeeWallExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPostCanSeeWallIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPrivatePlanner',
            fields=[
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='community_private_planner', serialize=False, to='users.user', verbose_name='Сообщество')),
                ('can_see_comments', models.CharField(choices=[('AC', 'Все пользователи'), ('M', 'Участники пространства или доски'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('FB', 'Друзья, кроме'), ('SF', 'Некоторые друзья'), ('MB', 'Участники, кроме'), ('SM', 'Некоторые участники')], default='M', max_length=2, verbose_name='Кто видит комментарии')),
                ('add_comments', models.CharField(choices=[('AC', 'Все пользователи'), ('M', 'Участники пространства или доски'), ('F', 'Друзья'), ('EO', 'Друзья и друзья друзей'), ('Y', 'Только я'), ('FB', 'Друзья, кроме'), ('SF', 'Некоторые друзья'), ('MB', 'Участники, кроме'), ('SM', 'Некоторые участники')], default='M', max_length=2, verbose_name='Кто добавляет комментарии')),
                ('vote_on', models.BooleanField(default=True, verbose_name='Реакции разрешены')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoAddCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoAddCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoAddItemExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoAddItemIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoCanSeeCommentExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoCanSeeCommentIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoCanSeeVideoExcludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityVideoCanSeeVideoIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.PositiveIntegerField(default=0, verbose_name='id назначателя')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='id пользователя')),
            ],
        ),
        migrations.RemoveField(
            model_name='communityprivategood',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='communityprivategood',
            name='good',
        ),
        migrations.RemoveField(
            model_name='communityprivatemusic',
            name='id',
        ),
        migrations.RemoveField(
            model_name='communityprivatemusic',
            name='music',
        ),
        migrations.RemoveField(
            model_name='communityprivatephoto',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='communityprivatephoto',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='communityprivatepost',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='communityprivatepost',
            name='wall',
        ),
        migrations.RemoveField(
            model_name='communityprivatevideo',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='communityprivatevideo',
            name='video',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='article',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='discussion',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='good',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='link',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='members',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='music',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='communitysectionsopen',
            name='video',
        ),
        migrations.AddField(
            model_name='communityprivategood',
            name='add_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто пишет комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivategood',
            name='add_item',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='YO', max_length=5, verbose_name='Кто добавляет товары и потом с этими товарами работает'),
        ),
        migrations.AddField(
            model_name='communityprivategood',
            name='can_see_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто видит комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivategood',
            name='vote_on',
            field=models.BooleanField(default=True, verbose_name='Реакции разрешены'),
        ),
        migrations.AddField(
            model_name='communityprivatemusic',
            name='add_item',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='YO', max_length=5, verbose_name='Кто добавляет аудио и потом с этими аудио работает'),
        ),
        migrations.AddField(
            model_name='communityprivatephoto',
            name='add_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто пишет комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivatephoto',
            name='add_item',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='YO', max_length=5, verbose_name='Кто добавляет фото и потом с этими фото работает'),
        ),
        migrations.AddField(
            model_name='communityprivatephoto',
            name='can_see_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто видит комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivatephoto',
            name='vote_on',
            field=models.BooleanField(default=True, verbose_name='Реакции разрешены'),
        ),
        migrations.AddField(
            model_name='communityprivatepost',
            name='add_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто пишет комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivatepost',
            name='add_item',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='YO', max_length=5, verbose_name='Кто добавляет записи и потом с этими записями работает'),
        ),
        migrations.AddField(
            model_name='communityprivatepost',
            name='can_see_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто видит комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivatepost',
            name='vote_on',
            field=models.BooleanField(default=True, verbose_name='Реакции разрешены'),
        ),
        migrations.AddField(
            model_name='communityprivatevideo',
            name='add_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто пишет комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivatevideo',
            name='add_item',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='YO', max_length=5, verbose_name='Кто добавляет видео и потом с этими видео работает'),
        ),
        migrations.AddField(
            model_name='communityprivatevideo',
            name='can_see_comment',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('YO', 'Только я'), ('MB', 'Подписчики, кроме'), ('SM', 'Некоторые подписчики')], default='AC', max_length=5, verbose_name='Кто видит комментарии'),
        ),
        migrations.AddField(
            model_name='communityprivatevideo',
            name='vote_on',
            field=models.BooleanField(default=True, verbose_name='Реакции разрешены'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_receive_message',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_board',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('M', 'Участники пространства или доски'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики'), ('MB', 'Участники, кроме'), ('SM', 'Некоторые участники')], default='M', max_length=3, verbose_name='Кто видит доски'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_doc',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто видит документы'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_good',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_members',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто видит друзей'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_music',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_photo',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_post',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто видит стену'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_video',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики')], default='AC', max_length=3, verbose_name='Кто пишет сообщения'),
        ),
        migrations.AddField(
            model_name='communitysectionsopen',
            name='can_see_workspace',
            field=models.CharField(choices=[('AC', 'Все пользователи'), ('M', 'Участники пространства или доски'), ('ME', 'Подписчики'), ('Y', 'Только я'), ('MEB', 'Подписчики, кроме'), ('SME', 'Некоторые подписчики'), ('MB', 'Участники, кроме'), ('SM', 'Некоторые участники')], default='M', max_length=3, verbose_name='Кто видит рабочие пространства и весь раздел'),
        ),
        migrations.AlterField(
            model_name='communityprivatemusic',
            name='community',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='community_private_audio', serialize=False, to='communities.community', verbose_name='Сообщество'),
        ),
    ]
