from django.db import models
from django.conf import settings


class UserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    ADVERTISER = 'R'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
        (ADVERTISER, 'Рекламодатель'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в профиле'
        verbose_name_plural = 'Полномочия в профиле'

class CommunityStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    ADVERTISER = 'R'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
        (ADVERTISER, 'Рекламодатель'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_community_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в сообществе'
        verbose_name_plural = 'Полномочия в сообществе'

class PostUserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в постах пользователей'
        verbose_name_plural = 'Полномочия в постах пользователей'

class GoodUserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='good_user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в товарах пользователей'
        verbose_name_plural = 'Полномочия в товарах пользователей'

class DocUserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doc_user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в документах'
        verbose_name_plural = 'Полномочия в документах'

class PhotoUserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photo_user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в фотографиях'
        verbose_name_plural = 'Полномочия в фотографиях'

class VideoUserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='video_user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в видеозаписях'
        verbose_name_plural = 'Полномочия в видеозаписях'

class AudioUserStaff(models.Model):
    ADMINISTRATOR = 'A'
    MODERATOR = 'M'
    EDITOR = 'E'
    LEVEL = (
        (ADMINISTRATOR, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (EDITOR, 'Редактор'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='music_user_staff', verbose_name="Особый пользователь")
    level = models.CharField(max_length=5, choices=LEVEL, blank=True, verbose_name="Уровень доступа")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Полномочия в аудиозаписях'
        verbose_name_plural = 'Полномочия в аудиозаписях'


class CanWorkStaffUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_user', verbose_name="Создатель персонала")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей")
    can_work_support = models.BooleanField(default=False, verbose_name="Может добавлять техподдержку")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала'
        verbose_name_plural = 'Создатели персонала'

class CanWorkStaffCommunity(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_community', verbose_name="Создатель персонала")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей")
    can_work_support = models.BooleanField(default=False, verbose_name="Может добавлять техподдержку")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала сообщетсв'
        verbose_name_plural = 'Создатели персонала сообщетсв'

class CanWorkStaffPostUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_post_user', verbose_name="Создатель персонала в записях")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов записей")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов записей")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов записей")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей записей")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала записей'
        verbose_name_plural = 'Создатели персонала записей'

class CanWorkStaffGoodUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_good_user', verbose_name="Создатель персонала в товарах")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов товаров")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов товаров")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов товаров")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей товаров")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала товаров'
        verbose_name_plural = 'Создатели персонала товаров'

class CanWorkStaffDocUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_doc_user', verbose_name="Создатель персонала в товарах")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов докуметов")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов докуметов")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов докуметов")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей докуметов")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала докуметов'
        verbose_name_plural = 'Создатели персонала докуметов'

class CanWorkStaffPhotoUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_photo_user', verbose_name="Создатель персонала в фотографиях")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов фотографий")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов фотографий")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов фотографий")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей фотографий")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала фотографий'
        verbose_name_plural = 'Создатели персонала фотографий'

class CanWorkStaffVideoUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_video_user', verbose_name="Создатель персонала в видеозаписях")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов видеозаписей")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов видеозаписей")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов видеозаписей")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей видеозаписей")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала видеозаписей'
        verbose_name_plural = 'Создатели персонала видеозаписей'

class CanWorkStaffAudioUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='can_work_staff_audio_user', verbose_name="Создатель персонала в аудиозаписях")
    can_work_administrator = models.BooleanField(default=False, verbose_name="Может добавлять администраторов аудиозаписей")
    can_work_moderator = models.BooleanField(default=False, verbose_name="Может добавлять модераторов аудиозаписей")
    can_work_editor = models.BooleanField(default=False, verbose_name="Может добавлять редакторов аудиозаписей")
    can_work_advertiser = models.BooleanField(default=False, verbose_name="Может добавлять рекламодателей аудиозаписей")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Создатель персонала аудиозаписей'
        verbose_name_plural = 'Создатели персонала аудиозаписей'


class ModerationCategory(models.Model):
    SEVERITY_CRITICAL, SEVERITY_HIGH, SEVERITY_MEDIUM, SEVERITY_LOW = 'C', 'H', 'M', 'L'
    SEVERITIES = (
        (SEVERITY_CRITICAL, 'Критический'),
        (SEVERITY_HIGH, 'Высокий'),
        (SEVERITY_MEDIUM, 'Средний'),
        (SEVERITY_LOW, 'Низкий'),
    )
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name="Название")
    title = models.CharField(max_length=64, blank=False, null=False, verbose_name="Заголовок")
    description = models.CharField(max_length=255, blank=False, null=False, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создано")
    severity = models.CharField(max_length=5, choices=SEVERITIES,verbose_name="Строгость")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория модерации'
        verbose_name_plural = 'Категории модерации'


USER, COMMUNITY = 'USE', 'COM'
POST_LIST, POST, POST_COMMENT = 'POL', 'POS', 'POSC'
PHOTO_LIST, PHOTO, PHOTO_COMMENT = 'PHL', 'PHO', 'PHOC'
DOC_LIST, DOC = 'DOL', 'DOC'
MUSIC_LIST, MUSIC = 'MUL', 'MUS'
VIDEO_LIST, VIDEO, VIDEO_COMMENT = 'VIL', 'VID', 'VIDC'
GOOD_LIST, GOOD, GOOD_COMMENT = 'GOL', 'GOO', 'GOOC'
TYPE = (
    (USER, 'Пользователь'), (COMMUNITY, 'Сообщество'),
    (MUSIC_LIST, 'Плейлист'), (MUSIC, 'Трек'),
    (POST_LIST, 'Список записей'), (POST, 'Запись'), (POST_COMMENT, 'Коммент к записи'),
    (DOC_LIST, 'Список документов'), (DOC, 'документ'),
    (PHOTO_LIST, 'Список фотографий'), (PHOTO, 'Фотография'), (PHOTO_COMMENT, 'Коммент к фотографии'),
    (VIDEO_LIST, 'Список роликов'), (VIDEO, 'Ролик'), (VIDEO_COMMENT, 'Коммент к ролику'),
    (GOOD_LIST, 'Список товаров'), (GOOD, 'Товар'), (GOOD_COMMENT, 'Коммент к товару'),
)

class Moderated(models.Model):
    # рассмотрение жалобы на объект, получаемфй по attach. Применение санкций или отвергание жалобы. При применении удаление жалоб-репортов
    PENDING, SUSPEND, BLOCKED, BANNER_GET, REJECTED, DELETED = 'P', 'S', 'B', 'BG', 'R', "D"
    STATUSES = (
        (PENDING, 'На рассмотрении'),
        (SUSPEND, 'Объект заморожен'),
        (BLOCKED, 'Объект заблокирован'),
        (BANNER_GET, 'Объекту присвоен баннер'),
        (REJECTED, 'Отвергнутый'),
    )
    description = models.TextField(max_length=300, blank=True, verbose_name="Описание")
    verified = models.BooleanField(default=False, verbose_name="Проверено")
    status = models.CharField(max_length=5, choices=STATUSES, default=PENDING, verbose_name="Статус")
    type = models.CharField(max_length=5, choices=TYPE, verbose_name="Класс объекта")
    object_id = models.PositiveIntegerField(default=0, verbose_name="id объекта")

    @classmethod
    def create_moderated_object(cls, type, object_id):
        return cls.objects.create(type=type, object_id=object_id)

    @classmethod
    def _get_or_create_moderated_object(cls, type, object_id):
        try:
            moderated_object = cls.objects.get(type=type, object_id=object_id)
            moderated_object.verified = False
            moderated_object.save(update_fields=['verified'])
        except cls.DoesNotExist:
            moderated_object = cls.create_moderated_object(type=type, object_id=object_id)
        return moderated_object

    @classmethod
    def get_or_create_moderated_object(cls, type, object_id):
        return cls._get_or_create_moderated_object(type=type, object_id=object_id)

    @property
    def reports_count(self):
        # кол-во жалоб на пользователя
        return self.reports.count()

    def is_verified(self):
        # проверен ли пользователь
        return self.verified
    def is_suspend(self):
        # Объект заморожен
        return self.status == Moderated.SUSPEND
    def is_pending(self):
        # Жалоба рассматривается
        return self.status == Moderated.PENDING
    def is_bloked(self):
        # Объект блокирован
        return self.status == Moderated.BLOCKED
    def is_banner(self):
        # Объект блокирован
        return self.status == Moderated.BANNER_GET
    def is_deleted(self):
        return self.status == ModeratedAudio.DELETED

    def create_suspend(self, manager_id, severity_int):
        from django.utils import timezone
        
        self.verified = True
        severity = None
        duration_of_penalty = None
        if severity_int == '4':
            duration_of_penalty = timezone.timedelta(days=30)
            severity = "C"
        elif severity_int == '3':
            duration_of_penalty = timezone.timedelta(days=7)
            severity = "H"
        elif severity_int == '2':
            duration_of_penalty = timezone.timedelta(days=3)
            severity = "M"
        elif severity_int == '1':
            duration_of_penalty = timezone.timedelta(hours=6)
            severity = "L"
        moderation_expiration = timezone.now() + duration_of_penalty
        ModerationPenalty.create_suspension_penalty(moderated_object=self, manager_id=manager_id, type=self.type, object_id=self.object_id, expiration=moderation_expiration)
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=severity)
        self.save()
    def create_block(self, manager_id):
        self.verified = True
        self.save()
        ModerationPenalty.create_block_penalty(moderated_object=self, manager_id=manager_id, type=self.type, object_id=self.object_id)
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.BLOCK)
    def create_warning_banner(self, manager_id):
        self.verified = True
        self.save()
        ModerationPenaltyUser.create_banner_penalty(moderated_object=self, manager_id=manager_id, type=self.type, object_id=self.object_id)
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.WARNING_BANNER)
    def create_deleted(self, manager_id):
        self.verified = True
        self.save()
        ModerationPenalty.create_delete_penalty(moderated_object=self, manager_id=manager_id, type=self.type, object_id=self.object_id)
        #AudioManageLog.objects.create(audio=audio_id, manager=manager_id, action_type=AudioManageLog.DELETED)
    def delete_deleted(self, manager_id):
        obj = ModerationPenalty.objects.get(moderated_object=self, type=self.type, object_id=self.object_id)
        obj.delete()
        self.delete()
        #AudioManageLog.objects.create(audio=audio_id, manager=manager_id, action_type=AudioManageLog.UNDELETED)
    def delete_suspend(self, manager_id):
        obj = ModerationPenalty.objects.get(moderated_object=self, type=self.type, object_id=self.object_id)
        obj.delete()
        self.delete()
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.UNSUSPENDED)
    def delete_block(self, manager_id):
        obj = ModerationPenalty.objects.get(moderated_object=self, type=self.type, object_id=self.object_id)
        obj.delete()
        self.delete()
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.UNBLOCK)
    def delete_warning_banner(self, manager_id):
        obj = ModerationPenalty.objects.get(moderated_object=self, type=self.type, object_id=self.object_id)
        obj.delete()
        self.delete()
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.NO_WARNING_BANNER)

    def unverify_moderation(self, manager_id):
        self.verified = False
        self.moderated_object.all().delete()
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.UNVERIFY)
        self.save()

    def reject_moderation(self, manager_id):
        self.verified = True
        self.status = ModeratedUser.REJECTED
        #UserManageLog.objects.create(user=user_id, manager=manager_id, action_type=UserManageLog.REJECT)
        self.save()

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Проверяемый объект'
        verbose_name_plural = 'Проверяемые объект'


class ModerationReport(models.Model):
    # жалобы на объект.
    PORNO = 'P'
    NO_CHILD = 'NC'
    SPAM = 'S'
    BROKEN = 'B'
    FRAUD = 'F'
    CLON = 'K'
    OLD_PAGE = 'OP'
    DRUGS = 'D'
    NO_MORALITY = 'NM'
    RHETORIC_HATE = "RH"
    UNETHICAL = "U"
    TYPE = (
        (PORNO, 'Порнография'),
        (NO_CHILD, 'Для взрослых'),
        (SPAM, 'Рассылка спама'),
        (BROKEN, 'Оскорбительное поведение'),
        (FRAUD, 'Мошенничество'),
        (CLON, 'Клон моей страницы'),
        (OLD_PAGE, 'Моя старая страница'),
        (DRUGS, 'Наркотики'),
        (NO_MORALITY, 'Не нравственный контент'),
        (RHETORIC_HATE, 'Риторика ненависти'),
        (UNETHICAL, 'Неэтичное поведение'),
    )

    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reporter', null=False, verbose_name="Репортер")
    moderated_object = models.ForeignKey(Moderated, on_delete=models.CASCADE, related_name='reports', null=False, verbose_name="Объект")
    description = models.CharField(max_length=300, blank=True, verbose_name="Описание")
    type = models.CharField(max_length=5, choices=TYPE, verbose_name="Тип нарушения")

    @classmethod
    def create_moderation_report(cls, reporter_id, _type, object_id, description, type):
        moderated_object = Moderated.get_or_create_moderated_object(type=_type, object_id=object_id)
        return cls.objects.create(reporter_id=reporter_id, type=type, description=description, moderated_object=moderated_object)

    def __str__(self):
        return self.reporter.get_full_name()

    class Meta:
        verbose_name = 'Жалоба на объект'
        verbose_name_plural = 'Жалобы на объект'


class ModerationPenalty(models.Model):
    # сами санкции против объекта.
    SUSPENSION, BLOCK, BANNER = 'S', 'B', 'BA'
    STATUSES = (
        (SUSPENSION, 'Приостановлено'), (BLOCK, 'Заблокировано'), (BANNER, 'Вывешен баннер'),
    )

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manager_penalties', verbose_name="Менеджер")
    expiration = models.DateTimeField(null=True, verbose_name="Окончание")
    moderated_object = models.ForeignKey(Moderated, on_delete=models.CASCADE, related_name='moderated_object', verbose_name="Объект")
    type = models.CharField(max_length=5, choices=TYPE, verbose_name="Класс объекта")
    object_id = models.PositiveIntegerField(default=0, verbose_name="id объекта")
    status = models.CharField(max_length=5, choices=STATUSES, verbose_name="Тип")

    @classmethod
    def create_suspension_penalty(cls, object_id, type, manager_id, moderated_object, expiration):
        try:
            obj = cls.objects.get(moderated_object=moderated_object)
            obj.delete()
            return cls.objects.create(moderated_object=moderated_object, manager_id=manager_id, object_id=object_id, type=type, status=cls.SUSPENSION, expiration=expiration)
        except:
            return cls.objects.create(moderated_object=moderated_object, manager_id=manager_id, object_id=object_id, type=type, status=cls.SUSPENSION, expiration=expiration)
    @classmethod
    def create_block_penalty(cls, object_id, type, manager_id, moderated_object):
        try:
            obj = cls.objects.get(moderated_object=moderated_object)
            obj.delete()
            return cls.objects.create(moderated_object=moderated_object, manager_id=manager_id, object_id=object_id, type=type, status=cls.BLOCK)
        except:
            return cls.objects.create(moderated_object=moderated_object, manager_id=manager_id, object_id=object_id, type=type, status=cls.BLOCK)
    @classmethod
    def create_banner_penalty(cls, object_id, type, manager_id, moderated_object):
        try:
            obj = cls.objects.get(moderated_object=moderated_object)
            obj.delete()
            return cls.objects.create(moderated_object=moderated_object, manager_id=manager_id, object_id=object_id, type=type, status=cls.BANNER)
        except:
            return cls.objects.create(moderated_object=moderated_object, manager_id=manager_id, object_id=object_id, type=type, status=cls.BANNER)

    def is_suspend(self):
        # Объект заморожен
        return self.status == SUSPENSION
    def is_bloked(self):
        # Объект блокирован
        return self.status == BLOCK
    def is_banner(self):
        # Объект блокирован
        return self.status == BANNER

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Оштрафованный объект'
        verbose_name_plural = 'Оштрафованные объект'
