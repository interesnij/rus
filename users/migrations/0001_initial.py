# Generated by Django 2.2.5 on 2019-10-18 20:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import users.helpers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('are_guidelines_accepted', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('invite_count', models.SmallIntegerField(default=0, verbose_name='Кол-во приглашений')),
                ('last_activity', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Активность')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserNotificationsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_comment_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления о комментариях к постам')),
                ('post_comment_reply_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления об ответах на комментарии к постам')),
                ('follow_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления о подписках')),
                ('connection_request_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления о заявках в друзья')),
                ('connection_confirmed_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления о приеме заявки в друзья')),
                ('community_invite_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления о приглашениях в сообщества')),
                ('post_comment_user_mention_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления об упоминаниях в комментариях к постам')),
                ('post_user_mention_notifications', models.BooleanField(default=True, verbose_name='Отправлять уведомления об упоминаниях в постам')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_settings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='UserBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_by_users', to=settings.AUTH_USER_MODEL)),
                ('blocker', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_blocks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('avatar', imagekit.models.fields.ProcessedImageField(null=True, upload_to=users.helpers.upload_to_user_avatar_directory, verbose_name='Аватар')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=users.helpers.upload_to_user_cover_directory, verbose_name='Фон')),
                ('bio', models.TextField(blank=True, max_length=1000, verbose_name='Биография')),
                ('followers_count_visible', models.BooleanField(default=False, verbose_name='Число подписчиков видно')),
                ('sity', models.CharField(blank=True, max_length=64, verbose_name='Местоположение')),
                ('status', models.CharField(blank=True, max_length=100, verbose_name='статус-слоган')),
                ('vk_url', models.URLField(blank=True, verbose_name='Ссылка на vk')),
                ('youtube_url', models.URLField(blank=True, verbose_name='Ссылка на youtube')),
                ('facebook_url', models.URLField(blank=True, verbose_name='Ссылка на facebook')),
                ('instagram_url', models.URLField(blank=True, verbose_name='Ссылка на instagram')),
                ('twitter_url', models.URLField(blank=True, verbose_name='Ссылка на twitter')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('user', models.OneToOneField(db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
                'index_together': {('id', 'user')},
            },
        ),
        migrations.AddIndex(
            model_name='userblock',
            index=models.Index(fields=['blocked_user', 'blocker'], name='users_userb_blocked_ab1a4e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='userblock',
            unique_together={('blocked_user', 'blocker')},
        ),
    ]
