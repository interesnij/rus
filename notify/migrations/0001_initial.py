# Generated by Django 2.2.16 on 2020-09-27 21:38

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к ролику'), ('PCR', 'ответил на Ваш комментарий к ролику'), ('L', 'понравилась Ваш ролик'), ('D', 'не понравилась Ваш ролик'), ('LC', 'понравился Ваш комментарий к ролику'), ('DC', 'не понравился Ваш комментарий к ролику'), ('LRC', 'понравился Ваш ответ на комментарий  к ролику'), ('DRC', 'не понравился Ваш ответ к комментарий к ролику'), ('R', 'поделился Вашим роликом')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - ролики пользователя',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - ролики пользователя',
            },
        ),
        migrations.CreateModel(
            name='VideoCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к записи сообщества'), ('PCR', 'ответил на комментарий к записи сообщества'), ('PUM', 'упомянул сообщество в записи'), ('PCUM', 'упомянул сообщество в комментарии к записи'), ('L', 'понравилась запись сообщества'), ('D', 'не понравилась запись сообщества'), ('LC', 'понравился комментарий в сообществе'), ('DC', 'не понравился комментарий в сообществе'), ('R', 'поделился записью сообщества')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - ролики сообщества',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - ролики сообщества',
            },
        ),
        migrations.CreateModel(
            name='UserNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('CR', 'подал заявку в друзья'), ('CC', 'подтвердил, что он Ваш друг'), ('CI', 'пригласил Вас в сообщество')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления пользователя',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление пользователя',
            },
        ),
        migrations.CreateModel(
            name='UserCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('verb', models.CharField(choices=[('CR', 'подал заявку в сообщество'), ('CC', 'принят в сообщество'), ('J', 'вступил в сообщество')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_user_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления сообщества',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление сообщества',
            },
        ),
        migrations.CreateModel(
            name='PostNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к записи'), ('PCR', 'ответил на Ваш комментарий к записи'), ('PUM', 'упомянул Вас в записи'), ('PCUM', 'упомянул Вас в комментарии к записи'), ('L', 'понравилась Ваша запись'), ('D', 'не понравилась Ваша запись'), ('LC', 'понравился Ваш комментарий к записи'), ('DC', 'не понравился Ваш комментарий к записи'), ('LRC', 'понравился Ваш ответ на комментарий  к записи'), ('DRC', 'не понравился Ваш ответ к комментарий к записи'), ('R', 'поделился Вашей записью')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - записи пользователя',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - записи пользователя',
            },
        ),
        migrations.CreateModel(
            name='PostCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к записи сообщества'), ('PCR', 'ответил на комментарий к записи сообщества'), ('PUM', 'упомянул сообщество в записи'), ('PCUM', 'упомянул сообщество в комментарии к записи'), ('L', 'понравилась запись сообщества'), ('D', 'не понравилась запись сообщества'), ('LC', 'понравился комментарий в сообществе'), ('DC', 'не понравился комментарий в сообществе'), ('R', 'поделился записью сообщества')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_post_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - записи сообщества',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - записи сообщества',
            },
        ),
        migrations.CreateModel(
            name='PhotoNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к изображению'), ('PCR', 'ответил на Ваш комментарий к изображению'), ('L', 'понравилось Ваше изображение'), ('D', 'не понравилось Ваше изображение'), ('LC', 'понравился Ваш комментарий к изображению'), ('DC', 'не понравился Ваш комментарий к изображению'), ('LRC', 'понравился Ваш ответ на комментарий к изображению'), ('DRC', 'не понравился Ваш ответ к комментарий к изображению'), ('R', 'поделился Вашим изображением')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - фотографии пользователя',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - фотографии пользователя',
            },
        ),
        migrations.CreateModel(
            name='PhotoCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к изображению сообщества'), ('PCR', 'ответил на комментарий к изображению сообщества'), ('L', 'понравилось изображение сообщества'), ('D', 'не понравилось изображение сообщества'), ('LC', 'понравился комментарий к изображению сообщества'), ('DC', 'не понравился комментарий к изображению сообщества'), ('LRC', 'понравился ответ на комментарий к изображению сообщества'), ('DRC', 'не понравился ответ к комментарий к изображению сообщества'), ('R', 'поделился изображением сообщества')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_photo_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Сообщество')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - фотографии сообщества',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - фотографии сообщества',
            },
        ),
        migrations.CreateModel(
            name='GoodNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к товару'), ('PCR', 'ответил на Ваш комментарий к товару'), ('L', 'понравился Ваш товар'), ('D', 'не понравился Ваш товар'), ('LC', 'понравился Ваш комментарий к товару'), ('DC', 'не понравился Ваш комментарий к товару'), ('LRC', 'понравился Ваш ответ на комментарий к товару'), ('DRC', 'не понравился Ваш ответ к комментарий к товару'), ('R', 'поделился Вашим товаром')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - товары пользователя',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - товары пользователя',
            },
        ),
        migrations.CreateModel(
            name='GoodCommunityNotify',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('unread', models.BooleanField(default=True)),
                ('verb', models.CharField(choices=[('PC', 'оставил комментарий к товару сообщества'), ('PCR', 'ответил на комментарий к товару сообщества'), ('L', 'понравился товар сообщества'), ('D', 'не понравился товар сообщества'), ('LC', 'понравился комментарий к товару сообщества'), ('DC', 'не понравился комментарий к товару сообщества'), ('LRC', 'понравился ответ на комментарий к товару сообщества'), ('DRC', 'не понравился ответ к комментарий к товару сообщества'), ('R', 'поделился товаром сообщества')], max_length=5, verbose_name='Тип уведомления')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_good_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Сообщество')),
            ],
            options={
                'verbose_name_plural': 'Уведомления - товары сообщества',
                'ordering': ['-created'],
                'verbose_name': 'Уведомление - товары сообщества',
            },
        ),
        migrations.AddIndex(
            model_name='videonotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_vide_created_fcc923_brin'),
        ),
        migrations.AddIndex(
            model_name='videocommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_vide_created_5bfdc0_brin'),
        ),
        migrations.AddIndex(
            model_name='usernotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_user_created_66e4ae_brin'),
        ),
        migrations.AddIndex(
            model_name='usercommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_user_created_227a2e_brin'),
        ),
        migrations.AddIndex(
            model_name='postnotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_post_created_e59d59_brin'),
        ),
        migrations.AddIndex(
            model_name='postcommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_post_created_4bb373_brin'),
        ),
        migrations.AddIndex(
            model_name='photonotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_phot_created_261b99_brin'),
        ),
        migrations.AddIndex(
            model_name='photocommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_phot_created_a8f4fb_brin'),
        ),
        migrations.AddIndex(
            model_name='goodnotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_good_created_6e73f9_brin'),
        ),
        migrations.AddIndex(
            model_name='goodcommunitynotify',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='notify_good_created_1be254_brin'),
        ),
    ]
