# Generated by Django 3.2 on 2021-04-29 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='Описание')),
                ('verified', models.BooleanField(default=False, verbose_name='Проверено')),
                ('status', models.CharField(choices=[('P', 'На рассмотрении'), ('S', 'Объект заморожен'), ('B', 'Объект заблокирован'), ('BG', 'Объекту присвоен баннер'), ('R', 'Отвергнутый')], default='P', max_length=5, verbose_name='Статус')),
                ('type', models.CharField(choices=[('USE', 'Пользователь'), ('COM', 'Сообщество'), ('MUL', 'Плейлист'), ('MUS', 'Трек'), ('POL', 'Список записей'), ('POS', 'Запись'), ('POSC', 'Коммент к записи'), ('DOL', 'Список документов'), ('DOC', 'документ'), ('PHL', 'Список фотографий'), ('PHO', 'Фотография'), ('PHOC', 'Коммент к фотографии'), ('VIL', 'Список роликов'), ('VID', 'Ролик'), ('VIDC', 'Коммент к ролику'), ('GOL', 'Список товаров'), ('GOO', 'Товар'), ('GOOC', 'Коммент к товару')], max_length=5, verbose_name='Класс объекта')),
                ('object_id', models.PositiveIntegerField(default=0, verbose_name='id объекта')),
            ],
            options={
                'verbose_name': 'Проверяемый объект',
                'verbose_name_plural': 'Проверяемые объект',
            },
        ),
        migrations.CreateModel(
            name='ModerationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('severity', models.CharField(choices=[('C', 'Критический'), ('H', 'Высокий'), ('M', 'Средний'), ('L', 'Низкий')], max_length=5, verbose_name='Строгость')),
            ],
            options={
                'verbose_name': 'Категория модерации',
                'verbose_name_plural': 'Категории модерации',
            },
        ),
        migrations.CreateModel(
            name='VideoUserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='video_user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в видеозаписях',
                'verbose_name_plural': 'Полномочия в видеозаписях',
            },
        ),
        migrations.CreateModel(
            name='UserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор'), ('R', 'Рекламодатель')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в профиле',
                'verbose_name_plural': 'Полномочия в профиле',
            },
        ),
        migrations.CreateModel(
            name='PostUserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post_user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в постах пользователей',
                'verbose_name_plural': 'Полномочия в постах пользователей',
            },
        ),
        migrations.CreateModel(
            name='PhotoUserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='photo_user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в фотографиях',
                'verbose_name_plural': 'Полномочия в фотографиях',
            },
        ),
        migrations.CreateModel(
            name='ModerationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Описание')),
                ('type', models.CharField(choices=[('P', 'Порнография'), ('NC', 'Для взрослых'), ('S', 'Рассылка спама'), ('B', 'Оскорбительное поведение'), ('F', 'Мошенничество'), ('K', 'Клон моей страницы'), ('OP', 'Моя старая страница'), ('D', 'Наркотики'), ('NM', 'Не нравственный контент'), ('RH', 'Риторика ненависти'), ('U', 'Неэтичное поведение')], max_length=5, verbose_name='Тип нарушения')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='managers.moderated', verbose_name='Объект')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL, verbose_name='Репортер')),
            ],
            options={
                'verbose_name': 'Жалоба на объект',
                'verbose_name_plural': 'Жалобы на объект',
            },
        ),
        migrations.CreateModel(
            name='ModerationPenalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField(null=True, verbose_name='Окончание')),
                ('type', models.CharField(choices=[('USE', 'Пользователь'), ('COM', 'Сообщество'), ('MUL', 'Плейлист'), ('MUS', 'Трек'), ('POL', 'Список записей'), ('POS', 'Запись'), ('POSC', 'Коммент к записи'), ('DOL', 'Список документов'), ('DOC', 'документ'), ('PHL', 'Список фотографий'), ('PHO', 'Фотография'), ('PHOC', 'Коммент к фотографии'), ('VIL', 'Список роликов'), ('VID', 'Ролик'), ('VIDC', 'Коммент к ролику'), ('GOL', 'Список товаров'), ('GOO', 'Товар'), ('GOOC', 'Коммент к товару')], max_length=5, verbose_name='Класс объекта')),
                ('object_id', models.PositiveIntegerField(default=0, verbose_name='id объекта')),
                ('status', models.CharField(choices=[('S', 'Приостановлено'), ('B', 'Заблокировано'), ('BA', 'Вывешен баннер')], max_length=5, verbose_name='Тип')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_penalties', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderated_object', to='managers.moderated', verbose_name='Объект')),
            ],
            options={
                'verbose_name': 'Оштрафованный объект',
                'verbose_name_plural': 'Оштрафованные объект',
            },
        ),
        migrations.CreateModel(
            name='GoodUserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='good_user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в товарах пользователей',
                'verbose_name_plural': 'Полномочия в товарах пользователей',
            },
        ),
        migrations.CreateModel(
            name='DocUserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doc_user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в документах',
                'verbose_name_plural': 'Полномочия в документах',
            },
        ),
        migrations.CreateModel(
            name='CommunityStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор'), ('R', 'Рекламодатель')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_community_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в сообществе',
                'verbose_name_plural': 'Полномочия в сообществе',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffVideoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов видеозаписей')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов видеозаписей')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов видеозаписей')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей видеозаписей')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_video_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала в видеозаписях')),
            ],
            options={
                'verbose_name': 'Создатель персонала видеозаписей',
                'verbose_name_plural': 'Создатели персонала видеозаписей',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей')),
                ('can_work_support', models.BooleanField(default=False, verbose_name='Может добавлять техподдержку')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала')),
            ],
            options={
                'verbose_name': 'Создатель персонала',
                'verbose_name_plural': 'Создатели персонала',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffPostUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов записей')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов записей')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов записей')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей записей')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_post_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала в записях')),
            ],
            options={
                'verbose_name': 'Создатель персонала записей',
                'verbose_name_plural': 'Создатели персонала записей',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffPhotoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов фотографий')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов фотографий')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов фотографий')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей фотографий')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_photo_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала в фотографиях')),
            ],
            options={
                'verbose_name': 'Создатель персонала фотографий',
                'verbose_name_plural': 'Создатели персонала фотографий',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffGoodUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов товаров')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов товаров')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов товаров')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей товаров')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_good_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала в товарах')),
            ],
            options={
                'verbose_name': 'Создатель персонала товаров',
                'verbose_name_plural': 'Создатели персонала товаров',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffDocUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов докуметов')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов докуметов')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов докуметов')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей докуметов')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_doc_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала в товарах')),
            ],
            options={
                'verbose_name': 'Создатель персонала докуметов',
                'verbose_name_plural': 'Создатели персонала докуметов',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffCommunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей')),
                ('can_work_support', models.BooleanField(default=False, verbose_name='Может добавлять техподдержку')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_community', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала')),
            ],
            options={
                'verbose_name': 'Создатель персонала сообщетсв',
                'verbose_name_plural': 'Создатели персонала сообщетсв',
            },
        ),
        migrations.CreateModel(
            name='CanWorkStaffAudioUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_work_administrator', models.BooleanField(default=False, verbose_name='Может добавлять администраторов аудиозаписей')),
                ('can_work_moderator', models.BooleanField(default=False, verbose_name='Может добавлять модераторов аудиозаписей')),
                ('can_work_editor', models.BooleanField(default=False, verbose_name='Может добавлять редакторов аудиозаписей')),
                ('can_work_advertiser', models.BooleanField(default=False, verbose_name='Может добавлять рекламодателей аудиозаписей')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='can_work_staff_audio_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель персонала в аудиозаписях')),
            ],
            options={
                'verbose_name': 'Создатель персонала аудиозаписей',
                'verbose_name_plural': 'Создатели персонала аудиозаписей',
            },
        ),
        migrations.CreateModel(
            name='AudioUserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, choices=[('A', 'Администратор'), ('M', 'Модератор'), ('E', 'Редактор')], max_length=5, verbose_name='Уровень доступа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='music_user_staff', to=settings.AUTH_USER_MODEL, verbose_name='Особый пользователь')),
            ],
            options={
                'verbose_name': 'Полномочия в аудиозаписях',
                'verbose_name_plural': 'Полномочия в аудиозаписях',
            },
        ),
    ]