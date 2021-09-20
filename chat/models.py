import uuid
from django.conf import settings
from django.db import models
from common.utils import try_except
from pilkit.processors import ResizeToFill, ResizeToFit
from chat.helpers import upload_to_chat_directory, validate_file_extension
from imagekit.models import ProcessedImageField
from django.contrib.postgres.indexes import BrinIndex
from django.db.models import Q
from common.model.other import Stickers


class Chat(models.Model):
    PRIVATE, MANAGER, PROCESSING, GROUP, PRIVATE_FIXED, GROUP_FIXED = 'PRI', 'MAN', '_PRO', 'GRO', '_FIXT', '_FIXG'
    DELETED_PRIVATE, DELETED_GROUP, DELETED_MANAGER, DELETED_PRIVATE_FIXED, DELETED_GROUP_FIXED = '_DEL', '_DELG', '_DELM', '_DELPF', '_DELGF'
    CLOSED_PRIVATE, CLOSED_GROUP, CLOSED_MANAGER, CLOSED_PRIVATE_FIXED, CLOSED_GROUP_FIXED = '_CLO', '_CLOG', '_CLOM', '_CLOPF', '_CLOGF'

    ALL_CAN, CREATOR, CREATOR_ADMINS = 1,2,3

    TYPE = (
        (PRIVATE, 'Пользовательский'),(MANAGER, 'Созданный персоналом'),(PROCESSING, 'Обработка'),(PRIVATE_FIXED, 'Закреплённый приватный'),(GROUP_FIXED, 'Закреплённый групповой'),
        (DELETED_PRIVATE, 'Удалённый приватный'),(DELETED_GROUP, 'Удалённый групповой'),(DELETED_MANAGER, 'Удалённый менеджерский'),(DELETED_PRIVATE_FIXED, 'Удалённый приватный закреплённый'),(DELETED_GROUP_FIXED, 'Удалённый групповой закреплённый'),
        (CLOSED_PRIVATE, 'Закрытый приватный'),(CLOSED_GROUP, 'Закрытый групповой'),(CLOSED_MANAGER, 'Закрытый менеджерский'),(CLOSED_PRIVATE_FIXED, 'Закрытый закреплённый приватный'),(CLOSED_GROUP_FIXED, 'Закрытый групповой закреплённый'),
    )
    ALL_PERM = ((ALL_CAN, 'Все участники'),(CREATOR, 'Создатель'),(CREATOR_ADMINS, 'Создатель и админы'),)
    ADMIN_PERM = ((CREATOR, 'Создатель'),(CREATOR_ADMINS, 'Создатель и админы'),)

    name = models.CharField(max_length=100, blank=True, verbose_name="Название")
    type = models.CharField(blank=False, null=False, choices=TYPE, default=PROCESSING, max_length=6, verbose_name="Тип чата")
    image = ProcessedImageField(blank=True, format='JPEG',options={'quality': 100},upload_to=upload_to_chat_directory,processors=[ResizeToFit(width=100, height=100,)])
    description = models.CharField(max_length=200, blank=True, verbose_name="Описание")
    community = models.ForeignKey('communities.Community', related_name='community_chat', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Сообщество")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='chat_creator', null=True, blank=False, verbose_name="Создатель")
    created = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    """ Полномочия в чате """
    can_add_members = models.PositiveSmallIntegerField(choices=ALL_PERM, default=1, verbose_name="Кто приглашает участников")
    can_edit_info = models.PositiveSmallIntegerField(choices=ALL_PERM, default=1, verbose_name="Кто редактирует информацию")
    can_fix_item = models.PositiveSmallIntegerField(choices=ALL_PERM, default=1, verbose_name="Кто закрепляет сообщения")
    can_mention = models.PositiveSmallIntegerField(choices=ALL_PERM, default=1, verbose_name="Кто упоминает о беседе")
    can_add_admin = models.PositiveSmallIntegerField(choices=ADMIN_PERM, default=1, verbose_name="Кто назначает админов")

    class Meta:
        verbose_name = "Беседа"
        verbose_name_plural = "Беседы"
        indexes = (BrinIndex(fields=['created']),)
        ordering = ["order"]

    def __str__(self):
        return self.creator.get_full_name()

    def is_private(self):
        return self.type == Chat.PRIVATE
    def is_group(self):
        return self.type == Chat.GROUP
    def is_manager(self):
        return self.type == Chat.MANAGER
    def is_open(self):
        return self.type[0] != "_"
    def is_muted(self, user_id):
        chat_user = ChatUsers.objects.get(chat_id=self.pk, user_id=user_id)
        return chat_user.beep()

    def get_members(self):
        from users.models import User
        return User.objects.filter(chat_users__chat__pk=self.pk)

    def get_recipients(self, exclude_creator_pk):
        from users.models import User
        return User.objects.filter(chat_users__chat__pk=self.pk).exclude(pk=exclude_creator_pk)

    def get_recipients_2(self, exclude_creator_pk):
        return ChatUsers.objects.filter(chat_id=self.pk).exclude(user_id=exclude_creator_pk)

    def get_members_ids(self):
        users = self.get_members().values('id')
        return [_user['id'] for _user in users]

    def get_recipients_ids(self, exclude_creator_pk):
        users = self.get_recipients(exclude_creator_pk).values('id')
        return [i['id'] for i in users]

    def get_members_count(self):
        return self.get_members().values('id').count()

    def get_members_count_ru(self):
        count = self.get_members_count()

        a, b = count % 10, count % 100
        if (a == 1) and (b != 11):
            return str(count) + " участник"
        elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
            return str(count) + " участника"
        else:
            return str(count) + " участников"

    def get_first_message(self, user_id):
        query = Q(recipient_id=user_id)|Q(type=Message.MANAGER)
        query.add(~Q(type__contains="_"), Q.AND)
        return self.chat_message.filter(query).first()

    def get_messages(self):
        return self.chat_message.exclude(type__contains="_")

    def get_messages_uuids(self):
        messages = self.chat_message.exclude(type__contains="_").values('uuid')
        return [i['uuid'] for i in messages]

    def get_attach_photos(self):
        from gallery.models import Photo
        return Photo.objects.filter(message__uuid__in=self.get_messages_uuids())

    def get_unread_count_message(self, user_id):
        count = 0
        for message in Message.objects.filter(chat_id=self.pk,recipient_id=user_id, unread=True):
            if message.creator.pk != user_id:
                count += 1
        if count:
            return ''.join(['<span style="font-size: 80%;" class="tab_badge badge-success">', str(count), '</span>'])
        else:
            return ""

    def get_unread_message(self, user_id):
        return self.chat_message.filter(recipient_id=user_id, unread=True)

    def get_messages_for_recipient(self, user_id):
        query = Q(recipient_id=user_id)|Q(type=Message.MANAGER)
        query.add(~Q(type__contains="_"), Q.AND)
        return self.chat_message.filter(query)

    def get_last_message_created(self):
        if self.is_not_empty():
            return self.get_first_message().get_created()
        else:
            return ''

    def get_chat_member(self, user_id):
        members = self.chat_relation.exclude(user_id=user_id)
        return members[0].user
    def get_chat_user(self, user_id):
        try:
            members = self.chat_relation.exclude(user_id=user_id)
            return members[0]
        except:
            member = self.chat_relation.get(user_id=user_id)
            return members
    def get_chat_request_user(self, user_id):
        return self.chat_relation.get(user_id=user_id)

    def get_preview_message(self, user_id):
        first_message, is_read, creator_figure = self.get_first_message(user_id), '', ''

        if self.is_have_draft_message(user_id):
            message = self.get_draft_message(user_id)
            if message.get_type_text():
                preview_text = 'Черновик: ' + message.get_type_text()
            else:
                if first_message.creator.id == user_id:
                    preview_text = 'Вы: ' + first_message.get_type_text()
                else:
                    preview_text = first_message.get_type_text()
        else:
            if first_message.creator.id == user_id:
                preview_text = 'Вы: ' + first_message.get_type_text()
            else:
                preview_text = first_message.get_type_text()
        if first_message.is_manager():
            creator = first_message.creator
            message = first_message.copy
            preview_text = creator.get_full_name() + first_message.text + '<span class="underline">' + message.get_text_60() + '</span>'

        request_chat_user = self.get_chat_request_user(user_id)

        if user_id == first_message.creator.pk and not first_message.is_copy_reed():
            is_read = ' bg-light-secondary'
        if self.is_private():
            chat_user = self.get_chat_user(user_id)
            member = chat_user.user
            if self.image:
                figure = ''.join(['<figure><img src="', self.image.url, '" style="border-radius:50px;width:50px;" alt="image"></figure>'])
            elif member.s_avatar:
                figure = ''.join(['<figure><img src="', member.s_avatar.url, '" style="border-radius:50px;width:50px;" alt="image"></figure>'])
            else:
                figure = '<figure><svg fill="currentColor" class="svg_default svg_default_50" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/><path d="M0 0h24v24H0z" fill="none"/></svg></figure>'
            if self.name:
                 chat_name = self.name
            else:
                chat_name = member.get_full_name()
            if member.get_online():
                status = ' <span class="status bg-success"></span>'
            else:
                status = ''
            media_body = ''.join(['<div class="media-body"><h5 class="time-title mb-0">', chat_name, request_chat_user.get_beep_icon(), status, '<small class="float-right text-muted">', first_message.get_created(), '</small></h5><p class="mb-0', is_read ,'" style="white-space: nowrap;">', preview_text, '</p><span class="typed"></span></div>'])
            return ''.join(['<div class="media">', figure, media_body, self.get_unread_count_message(user_id), '</div>'])
        elif self.is_group():
            if self.image:
                figure = ''.join(['<figure><img src="', self.image.url, '" style="border-radius:50px;width:50px;" alt="image"></figure>'])
            else:
                figure = '<figure><img src="/static/images/group_chat.jpg" style="border-radius:50px;width:50px;" alt="image"></figure>'
            if self.name:
                 chat_name = self.name
            else:
                chat_name = "Групповой чат"
            media_body = ''.join(['<div class="media-body"><h5 class="time-title mb-0">', chat_name, request_chat_user.get_beep_icon(), '<small class="float-right text-muted">', first_message.get_created(), '</small></h5><p class="mb-0', is_read ,'" style="white-space: nowrap;">', preview_text, '</p></div>'])
            return ''.join(['<div class="media">', figure, media_body, self.get_unread_count_message(user_id), '</div>'])

    def get_avatars(self):
        urls = []
        for user in self.chat_relation.all()[:10]:
            urls += [user.user.get_s_avatar()]
        return urls

    def get_header_private_chat(self, user_id):
        buttons = '<span class="console_btn_other btn_default" style="display:none;"><span class="one_message"><span tooltip="Закрепить" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_fixed" fill="currentColor" viewBox="0 0 24 24"><g><rect fill="none" height="24" width="24"/></g><g><path d="M16,9V4l1,0c0.55,0,1-0.45,1-1v0c0-0.55-0.45-1-1-1H7C6.45,2,6,2.45,6,3v0 c0,0.55,0.45,1,1,1l1,0v5c0,1.66-1.34,3-3,3h0v2h5.97v7l1,1l1-1v-7H19v-2h0C17.34,12,16,10.66,16,9z" fill-rule="evenodd"/></g></svg></span><span tooltip="Ответить" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_reply" viewBox="0 0 24 24" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"/></svg></span><span tooltip="Пожаловаться" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_claim" viewBox="0 0 24 24" fill="currentColor"><path d="M11 15h2v2h-2v-2zm0-8h2v6h-2V7zm.99-5C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/></svg></span><span tooltip="Редактировать" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_edit" fill="currentColor" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg></span></span><span tooltip="Отметить как важное" flow="up"><svg class="toggle_message_favourite svg_default_30 mr-1 pointer" fill="currentColor" enable-background="new 0 0 24 24" viewBox="0 0 24 24"><g><rect x="0"></rect><polygon points="14.43,10 12,2 9.57,10 2,10 8.18,14.41 5.83,22 12,17.31 18.18,22 15.83,14.41 22,10"></polygon></g></svg></span><span tooltip="Удалить" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_delete" viewBox="0 0 24 24" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM8 9h8v10H8V9zm7.5-5l-1-1h-5l-1 1H5v2h14V4h-3.5z"/></svg></span><span tooltip="Переслать" flow="up"><svg class="svg_default_30 pointer u_message_transfer" viewBox="0 0 24 24" fill="currentColor"><path d="m0 0h24v24h-24z" fill="none"/><path fill="currentColor" d="m12.1 7.87v-3.47a1.32 1.32 0 0 1 2.17-1l8.94 7.6a1.32 1.32 0 0 1 .15 1.86l-.15.15-8.94 7.6a1.32 1.32 0 0 1 -2.17-1v-3.45c-4.68.11-8 1.09-9.89 2.87a1.15 1.15 0 0 1 -1.9-1.11c1.53-6.36 5.51-9.76 11.79-10.05zm1.8-2.42v4.2h-.9c-5.3 0-8.72 2.25-10.39 6.86 2.45-1.45 5.92-2.16 10.39-2.16h.9v4.2l7.71-6.55z" /></svg></span></span>'
        chat_user = self.get_chat_user(user_id)
        request_chat_user = self.get_chat_request_user(user_id)
        member = chat_user.user
        if self.image:
            figure = ''.join(['<figure><img src="', self.image.url, '" style="border-radius:30px;width:30px;" alt="image"></figure>'])
        elif member.s_avatar:
            figure = ''.join(['<figure><img src="', member.s_avatar.url,'" style="border-radius:30px;width:30px;" alt="image"></figure>'])
        else:
            figure = '<figure><svg fill="currentColor" class="svg_default_30" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/><path d="M0 0h24v24H0z" fill="none"/></svg></figure>'
        if self.name:
             chat_name = self.name
        else:
            chat_name = member.get_full_name()
        media_body = ''.join(['<div class="media-body" style="overflow: inherit;"><h5 class="time-title mb-0"><a href="', member.get_link(), '" target="_blank">', chat_name, request_chat_user.get_beep_icon(), '</a></h5><span class="mt-1 mb-2 target_display"><span class="type_display small" style="position:absolute;left:72px;top: 19px;">', member.get_online_status(), '</span>', buttons, '</span></div>'])
        return ''.join(['<a href="', member.get_link(), '" target="_blank">', figure, '</a>', media_body])

    def get_header_group_chat(self, user_id):
        chat_user = self.get_chat_user(user_id)
        request_chat_user = self.get_chat_request_user(user_id)
        buttons = '<span class="console_btn_other btn_default" style="display:none;padding-top:5px"><span class="one_message"><span tooltip="Закрепить" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_fixed" fill="currentColor" viewBox="0 0 24 24"><g><rect fill="none" height="24" width="24"/></g><g><path d="M16,9V4l1,0c0.55,0,1-0.45,1-1v0c0-0.55-0.45-1-1-1H7C6.45,2,6,2.45,6,3v0 c0,0.55,0.45,1,1,1l1,0v5c0,1.66-1.34,3-3,3h0v2h5.97v7l1,1l1-1v-7H19v-2h0C17.34,12,16,10.66,16,9z" fill-rule="evenodd"/></g></svg></span><span tooltip="Ответить" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_reply" viewBox="0 0 24 24" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"/></svg></span><span tooltip="Пожаловаться" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_claim" viewBox="0 0 24 24" fill="currentColor"><path d="M11 15h2v2h-2v-2zm0-8h2v6h-2V7zm.99-5C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/></svg></span><span tooltip="Редактировать" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_edit" fill="currentColor" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg></span></span><span tooltip="Отметить как важное" flow="up"><svg class="toggle_message_favourite svg_default_30 mr-1 pointer" fill="currentColor" enable-background="new 0 0 24 24" viewBox="0 0 24 24"><g><rect x="0"></rect><polygon points="14.43,10 12,2 9.57,10 2,10 8.18,14.41 5.83,22 12,17.31 18.18,22 15.83,14.41 22,10"></polygon></g></svg></span><span tooltip="Удалить" flow="up"><svg class="svg_default_30 mr-1 pointer u_message_delete" viewBox="0 0 24 24" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM8 9h8v10H8V9zm7.5-5l-1-1h-5l-1 1H5v2h14V4h-3.5z"/></svg></span><span tooltip="Переслать" flow="up"><svg class="svg_default_30 pointer u_message_transfer" viewBox="0 0 24 24" fill="currentColor"><path d="m0 0h24v24h-24z" fill="none"/><path fill="currentColor" d="m12.1 7.87v-3.47a1.32 1.32 0 0 1 2.17-1l8.94 7.6a1.32 1.32 0 0 1 .15 1.86l-.15.15-8.94 7.6a1.32 1.32 0 0 1 -2.17-1v-3.45c-4.68.11-8 1.09-9.89 2.87a1.15 1.15 0 0 1 -1.9-1.11c1.53-6.36 5.51-9.76 11.79-10.05zm1.8-2.42v4.2h-.9c-5.3 0-8.72 2.25-10.39 6.86 2.45-1.45 5.92-2.16 10.39-2.16h.9v4.2l7.71-6.55z" /></svg></span></span>'
        if self.image:
            figure = ''.join(['<figure><img src="', self.image.url, '" style="border-radius:30px;width:30px;" alt="image"></figure>'])
        else:
            avatars = ''
            for figure in self.get_avatars():
                avatars += figure
        if self.name:
             chat_name = self.name
        else:
            chat_name = "Групповой чат"
        media_body = ''.join(['<div class="media-body" style="overflow: inherit;"><h5 class="time-title mb-0 pointer u_chat_settings">', chat_name, request_chat_user.get_beep_icon(), '</h5><span class="mt-1 mb-2 target_display"><span class="type_display small" style="position:absolute;left:25px;top: 19px;">', self.get_members_count_ru(), '</span>', buttons, '</span></div>'])
        return ''.join([media_body, avatars])

    def is_not_empty(self):
        return self.chat_message.exclude(type__contains="_").exists()

    def add_administrator(self, user):
        member = self.chat_relation.get(user=user)
        member.is_administrator = True
        member.save(update_fields=["is_administrator"])
        return member
    def remove_administrator(self, user):
        member = self.chat_relation.get(user=user)
        member.is_administrator = False
        member.save(update_fields=["is_administrator"])
        return member

    def get_attach_photos(self):
        if "pho" in self.attach:
            query = []
            from gallery.models import Photo

            for item in self.attach.split(","):
                if item[:3] == "pho":
                    query.append(item[3:])
        return Photo.objects.filter(id__in=query)

    def get_attach_videos(self):
        if "pho" in self.attach:
            query = []
            from video.models import Video
            for item in self.attach.split(","):
                if item[:3] == "vid":
                    query.append(item[3:])
        return Video.objects.filter(id__in=query)

    def get_draft_message(self, user_id):
        return Message.objects.filter(chat_id=self.pk, creator_id=user_id, type=Message.DRAFT).first()

    def is_have_draft_message(self, user_id):
        return Message.objects.filter(chat_id=self.pk, creator_id=user_id, type=Message.DRAFT).exists()

    def get_first_fix_message(self):
        if MessageFixed.objects.filter(chat_id=self.id).exists():
            return MessageFixed.objects.filter(chat_id=self.id).first()

    def get_fixed_messages(self):
        return MessageFixed.objects.filter(chat_id=self.id)

    def get_fix_message_count(self):
        if MessageFixed.objects.filter(chat_id=self.id).exists():
            return MessageFixed.objects.filter(chat_id=self.id).values("pk").count()
        else:
            return 0

    def get_fix_message_count_ru(self):
        count = self.get_fix_message_count()

        a, b = count % 10, count % 100
        if (a == 1) and (b != 11):
            return str(count) + " сообщение"
        elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
            return str(count) + " сообщения"
        else:
            return str(count) + " сообщений"


class ChatUsers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, related_name='chat_users', null=False, blank=False, verbose_name="Члены сообщества")
    chat = models.ForeignKey(Chat, db_index=False, on_delete=models.CASCADE, related_name='chat_relation', verbose_name="Чат")
    is_administrator = models.BooleanField(default=False, verbose_name="Это администратор")
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Создано")
    no_disturb = models.DateTimeField(blank=True, null=True, verbose_name='Не беспокоить до...')

    def __str__(self):
        return self.user.get_full_name()

    @classmethod
    def create_membership(cls, user, chat, is_administrator=False):
        membership = cls.objects.create(user=user, chat=chat, is_administrator=is_administrator)
        return membership

    def delete_membership(user, chat):
        if ChatUsers.objects.filter(user=user, chat=chat).exists():
            membership = ChatUsers.objects.get(user=user, chat=chat)
            membership.delete()
        else:
            pass

    def beep(self):
        if not self.no_disturb:
            return True
        else:
            from datetime import datetime
            return self.no_disturb < datetime.now()

    def get_beep_icon(self):
        if not self.beep():
            return ' <svg style="width: 17px;" enable-background="new 0 0 24 24" height="17px" viewBox="0 0 24 24" width="17px" fill="currentColor"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M4.34 2.93L2.93 4.34 7.29 8.7 7 9H3v6h4l5 5v-6.59l4.18 4.18c-.65.49-1.38.88-2.18 1.11v2.06c1.34-.3 2.57-.92 3.61-1.75l2.05 2.05 1.41-1.41L4.34 2.93zM10 15.17L7.83 13H5v-2h2.83l.88-.88L10 11.41v3.76zM19 12c0 .82-.15 1.61-.41 2.34l1.53 1.53c.56-1.17.88-2.48.88-3.87 0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zm-7-8l-1.88 1.88L12 7.76zm4.5 8c0-1.77-1.02-3.29-2.5-4.03v1.79l2.48 2.48c.01-.08.02-.16.02-.24z"/></svg>'
        else:
            return ''

    class Meta:
        unique_together = (('user', 'chat'),)
        indexes = [
            models.Index(fields=['chat', 'user']),
            models.Index(fields=['chat', 'user', 'is_administrator'])
            ]
        verbose_name = 'участник беседы'
        verbose_name_plural = 'участники бесед'


class Message(models.Model):
    MANAGER, PROCESSING, PUBLISHED, EDITED, DELETED, CLOSED, FIXED, FIXED_EDITED, DRAFT = 'MAN', '_PRO','PUB','EDI','_DEL','_CLO','_FIX','_FIXE','_DRA'
    DELETED_FIXED, DELETED_EDITED_FIXED, DELETED_EDITED, CLOSED_EDITED_FIXED, CLOSED_FIXED, CLOSED_EDITED = '_DELF','_DELFI','_DELE','_CLOFI','_CLOF','_CLOE'
    TYPE = (
        (MANAGER, 'Специальное'),(PROCESSING, 'Обработка'),(PUBLISHED, 'Опубликовано'),(DELETED, 'Удалено'),(EDITED, 'Изменено'),(CLOSED, 'Закрыто модератором'),(DRAFT, 'Черновик'),
        (DELETED_FIXED, 'Удалённый закрепленный'),(DELETED_EDITED_FIXED, 'Удалённый измененный закрепленный'),(DELETED_EDITED, 'Удалённый измененный'),(CLOSED_EDITED, 'Закрытый измененный'),(CLOSED_EDITED_FIXED, 'Закрытый измененный закрепленный'),(CLOSED_FIXED, 'Закрытый закрепленный'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='message_creator', verbose_name="Создатель", null=True, on_delete=models.SET_NULL)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='message_recipient', verbose_name="Получаетель", null=True, on_delete=models.SET_NULL)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat_message")
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name="message_thread")
    copy = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name="message_copy")
    sticker = models.ForeignKey(Stickers, blank=True, null=True, on_delete=models.CASCADE, related_name="+")
    repost = models.ForeignKey("posts.Post", on_delete=models.CASCADE, null=True, blank=True, related_name='post_message')
    transfer = models.ManyToManyField("self", blank=True, related_name='+')

    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, blank=True)
    unread = models.BooleanField(default=True, db_index=True, verbose_name="Не прочитано")
    type = models.CharField(choices=TYPE, default=PROCESSING, max_length=6, verbose_name="Статус сообщения")
    attach = models.CharField(blank=True, max_length=200, verbose_name="Прикрепленные элементы")
    voice = models.FileField(blank=True, upload_to=upload_to_chat_directory, verbose_name="Голосовое сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["-created"]
        indexes = (BrinIndex(fields=['created']),)

    def __str__(self):
        return self.text

    def is_copy_reed(self):
        """ мы получаем копию сообщения любую. Если копия прочитана, значит возвращаем True
        Зачем это - при отрисовке первого сообщения правильно выводить кол-во непрочитанных. """
        for copy in self.message_copy.filter(copy=self).all():
            if not copy.unread:
                return True
        return False

    def get_draft_transfers_block(self):
        transfers = self.transfer.all()
        count = transfers.count()
        a = count % 10
        b = count % 100
        if (a == 1) and (b != 11):
            text = str(count) + " сообщение"
        elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
            text = str(count) + " сообщения"
        else:
            text = str(count) + " сообщений"
        if count > 1:
            text_2 = "Пересланные сообщения"
        else:
            text_2 = "Пересланное сообщение"
        inputs = ""
        for i in transfers:
            inputs += '<input type="hidden" name="transfer" value="' + str(i.uuid) + '" class="transfer">'
        return '<div><p>' + text_2 + '</p><div style="position:relative;padding-bottom:7px"><div><span class="pointer underline">' + text + '</span><span class="remove_parent_block pointer message_form_parent_block">x</span></div></div>' + inputs + '</div>'

    def is_edited(self):
        return self.type == "EDI"
    def is_manager(self):
        return self.type == Message.MANAGER

    def is_have_transfer(self):
        if self.transfer.exists():
            return True

    def get_count_attach(self):
        if self.attach:
            length = self.attach.split(",")
            return "files_" + str(len(length))
        else:
            return "files_0"

    def get_parent_message(self):
        if not self.parent:
            return '<div class="media p-1 pag">Нет ответа!</div>'
        parent = self.parent
        if parent.voice:
            preview = "Голосовое сообщение"
        if parent.sticker:
            preview = "Наклейка"
        if parent.attach:
            preview = "Вложения"
        else:
            preview = parent.text[:80]
        user = parent.creator

        return '<div class="media p-1" data-uuid="' + str(parent.uuid) + '" style="border-left: 1px solid rgba(0, 0, 0, 0.7)"><span style="padding-top: 6px;"><a href="' + user.get_link() + '" class="ajax"><img src="' + user.get_avatar() + '" style="border-radius:30px;width:30px;" alt="image"></a></span><div class="media-body" style="line-height: 1em;padding-left: 3px;"><p class="time-title mb-0"><a href="' + user.get_link()  + '" class="ajax">' + user.get_full_name() + '</a></p><small class="text-muted">' + parent.get_created() + '</small><p class="text">' + preview + '</p></div></div>'

    def is_message_in_favourite(self, user_id):
        return MessageFavourite.objects.filter(message=self, user_id=user_id).exists()

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def get_creator(self):
        return self.creator.user
    def get_recipient(self):
        return self.recipient.user

    def get_reseiver_ids(self):
        return self.chat.get_members_ids()

    def create_socket(self, recipient_id, beep_on):
        from asgiref.sync import async_to_sync
        from channels.layers import get_channel_layer

        channel_layer = get_channel_layer()
        payload = {
            'type': 'receive',
            'key': 'message',
            'message_id': str(self.uuid),
            'chat_id': str(self.chat.pk),
            'recipient_id': str(recipient_id),
            'name': "u_message_create",
            'beep': beep_on,
        }
        async_to_sync(channel_layer.group_send)('notification', payload)

    def get_format_attach(value):
        _attach = str(value)
        return _attach.replace("'", "").replace("[", "").replace("]", "").replace(" ", "").replace("<div class='attach_container'></div>", "")


    def get_or_create_chat_and_send_message(creator, user, repost, text, attach, voice, sticker):
        # получаем список чатов отправителя. Если получатель есть в одном из чатов, добавляем туда сообщение.
        # Если такого чата нет, создаем приватный чат, создаем по сообщению на каждого участника чата.
        from common.processing.message import get_message_processing

        chat_list, current_chat = creator.get_all_chats(), None
        for chat in chat_list:
            if user.pk in chat.get_members_ids() and chat.is_private():
                current_chat = chat
        if not current_chat:
            current_chat = Chat.objects.create(creator=creator, type=Chat.PRIVATE)
            ChatUsers.objects.create(user=creator, is_administrator=True, chat=current_chat)
            ChatUsers.objects.create(user=user, chat=current_chat)

        if voice:
            creator_message = Message.objects.create(chat=current_chat, creator=creator, recipient_id=creator.pk, repost=repost, voice=voice, type=Message.PUBLISHED)
        elif sticker:
            creator_message = Message.objects.create(chat=current_chat, creator=creator, recipient_id=creator.pk, repost=repost, sticker_id=sticker, type=Message.PUBLISHED)
            from common.model.other import UserPopulateStickers
            UserPopulateStickers.get_plus_or_create(user_pk=creator.pk, sticker_pk=sticker)
        else:
            creator_message = Message.objects.create(chat=current_chat, creator=creator, recipient_id=creator.pk, repost=repost, text=text, attach=Message.get_format_attach(attach), type=Message.PROCESSING)
        get_message_processing(creator_message, 'PUB')
        for recipient in chat.get_recipients_2(creator.pk):
            if voice:
                recipient_message = Message.objects.create(chat=current_chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, voice=voice, type=Message.PUBLISHED)
            elif sticker:
                recipient_message = Message.objects.create(chat=current_chat, copy=creator_message, sticker_id=sticker, recipient_id=recipient.user.pk, repost=repost, voice=voice, type=Message.PUBLISHED)
            else:
                recipient_message = Message.objects.create(chat=current_chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, text=text, attach=Message.get_format_attach(attach), type=Message.PROCESSING)
            get_message_processing(recipient_message, 'PUB')
            recipient_message.create_socket(recipient.user.pk, recipient.beep())

    def create_chat_append_members_and_send_message(creator, users_ids, text, attach, voice, sticker):
        # Создаем коллективный чат и добавляем туда всех пользователей из полученного списка
        from common.processing.message import get_message_processing

        chat = Chat.objects.create(creator=creator, type=Chat.GROUP)

        if voice:
            creator_message = Message.objects.create(chat=chat, creator=creator, recipient_id=creator.pk, repost=repost, voice=voice, type=Message.PUBLISHED)
        elif sticker:
            creator_message = Message.objects.create(chat=chat, creator=creator, recipient_id=creator.pk, repost=repost, sticker_id=sticker, type=Message.PUBLISHED)
            from common.model.other import UserPopulateStickers
            UserPopulateStickers.get_plus_or_create(user_pk=creator.pk, sticker_pk=sticker)
        else:
            creator_message = Message.objects.create(chat=chat, creator=creator, recipient_id=creator.pk, repost=repost, text=text, attach=Message.get_format_attach(attach), type=Message.PROCESSING)
        get_message_processing(creator_message, 'PUB')

        for recipient in chat.get_recipients_2(creator.pk):
            if voice:
                recipient_message = Message.objects.create(chat=chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, voice=voice, type=Message.PUBLISHED)
            elif sticker:
                recipient_message = Message.objects.create(chat=chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, sticker_id=sticker, type=Message.PUBLISHED)
            else:
                recipient_message = Message.objects.create(chat=chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, text=text, attach=Message.get_format_attach(attach), type=Message.PROCESSING)
            recipient_message.create_socket(recipient.user.pk, recipient.beep())
            get_message_processing(creator_message, 'PUB')
    def send_message(chat, creator, repost, parent, text, attach, voice, sticker, transfer):
        # программа для отсылки сообщения в чате
        from common.processing.message import get_message_processing

        if parent:
            parent_id = parent
        else:
            parent_id = None
        if voice:
            creator_message = Message.objects.create(chat=chat, creator=creator, recipient_id=creator.pk, repost=repost, voice=voice, parent_id=parent_id, type=Message.PUBLISHED)
        elif sticker:
            creator_message = Message.objects.create(chat=chat, creator=creator, recipient_id=creator.pk, repost=repost, sticker_id=sticker, parent_id=parent_id, type=Message.PUBLISHED)
            from common.model.other import UserPopulateStickers
            UserPopulateStickers.get_plus_or_create(user_pk=creator.pk, sticker_pk=sticker)
        else:
            if text:
                import re
                ids = re.findall(r'data-pk="(?P<pk>\d+)"', text)
                if ids:
                    from common.model.other import UserPopulateSmiles
                    for id in ids:
                        UserPopulateSmiles.get_plus_or_create(user_pk=creator.pk, smile_pk=id)
            creator_message = Message.objects.create(chat=chat, creator=creator, recipient_id=creator.pk, repost=repost, text=text, attach=Message.get_format_attach(attach), parent_id=parent_id, type=Message.PROCESSING)
            if transfer:
                for i in transfer:
                    m = Message.objects.get(uuid=i)
                    creator_message.transfer.add(m)
            if chat.is_have_draft_message(creator.pk):
                message = chat.get_draft_message(creator.pk)
                message.text = ""
                message.attach = ""
                message.parent_id = None
                message.transfer.clear()
                message.save(update_fields=["text","attach","parent_id"])
        get_message_processing(creator_message, 'PUB')

        for recipient in chat.get_recipients_2(creator.pk):
            if voice:
                recipient_message = Message.objects.create(chat=chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, voice=voice, parent_id=parent_id, type=Message.PUBLISHED)
            elif sticker:
                recipient_message = Message.objects.create(chat=chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, sticker_id=sticker, parent_id=parent_id, type=Message.PUBLISHED)
            else:
                recipient_message = Message.objects.create(chat=chat, copy=creator_message, creator=creator, recipient_id=recipient.user.pk, repost=repost, text=text, parent_id=parent_id, attach=Message.get_format_attach(attach), type=Message.PROCESSING)
            get_message_processing(recipient_message, 'PUB')
            recipient_message.create_socket(recipient.user.pk, recipient.beep())
        return creator_message

    def save_draft_message(chat, creator, parent, text, attach, transfer):
        # программа для сохранения черновика сообщения в чате, а также посылания сокета
        # всем участникам чата, что создатель черновика набирает сообщение
        from asgiref.sync import async_to_sync
        from channels.layers import get_channel_layer

        if parent:
            parent_id = parent
        else:
            parent_id = None

        if text:
            import re
            ids = re.findall(r'data-pk="(?P<pk>\d+)"', text)
            if ids:
                from common.model.other import UserPopulateSmiles
                for id in ids:
                    UserPopulateSmiles.get_plus_or_create(user_pk=creator.pk, smile_pk=id)

        if chat.is_have_draft_message(creator.pk):
            message = chat.get_draft_message(creator.pk)
            message.text = text
            message.attach = Message.get_format_attach(attach)
            message.parent_id = parent_id
            message.save(update_fields=["text","attach","parent_id"])

        else:
            message = Message.objects.create(chat=chat, creator_id=creator.pk, recipient_id=creator.pk, text=text, attach=Message.get_format_attach(attach), parent_id=parent_id, type=Message.DRAFT)
        message.transfer.clear()
        if transfer:
            for i in transfer:
                m = Message.objects.get(uuid=i)
                message.transfer.add(m)

        channel_layer = get_channel_layer()
        payload = {
            'type': 'receive',
            'key': 'message',
            'chat_id': chat.pk,
            'recipient_ids': str(chat.get_recipients_ids(creator.pk)),
            'name': "u_message_typed",
            'user_name': creator.first_name,
        }
        async_to_sync(channel_layer.group_send)('notification', payload)

    def fixed_message_for_user_chat(self, creator):
        """
            Мы должны пометить все сообшения ветки как FIXED.
            Для этого выясняем: это родительское сообщение, или имеет такое в поле copy.
            Его и все копированные помечаем и сохраняем. Создаем запись в таблице закрепленных сообщений,
            и в поле copy записываем сообшение, которое закрепляем. Мера нужна для показывания людям сообщения,
            которое открепили, чтобы новое поле не создавать, их и так много.
            Также создаем сокеты, чтобы участники чата увидели новое инфо-сообщение сразу
        """
        if self.copy:
            message = self.copy
            if message.type == "PUB":
                message.type = "_FIX"
            else:
                message.type = "_FIXE"
            message.save(update_fields=['type'])
            for i in Message.objects.filter(copy_id=message.pk):
                if i.type == "PUB":
                    i.type = "_FIX"
                else:
                    i.type = "_FIXE"
                i.save(update_fields=['type'])
        else:
            if self.type == "PUB":
                self.type = "_FIX"
            else:
                self.type = "_FIXE"
            self.save(update_fields=['type'])
            for i in Message.objects.filter(copy_id=self.pk):
                if i.type == "PUB":
                    i.type = "_FIX"
                else:
                    i.type = "_FIXE"
                i.save(update_fields=['type'])

        self.save(update_fields=['type'])
        fixed_message = MessageFixed.objects.create(chat_id=self.chat.id,creator_id=creator.id,message=self)
        if creator.is_women():
            var = " закрепила"
        else:
            var = " закрепил"
        text = var + " сообщение "
        info_message = Message.objects.create(chat_id=self.chat.id,creator_id=creator.id,type=Message.MANAGER,text=text,copy=self)
        for recipient in self.chat.get_recipients_2(creator.pk):
            info_message.create_socket(recipient.user.pk, recipient.beep())
        return info_message

    def unfixed_message_for_user_chat(self, creator):
        """
            Мы должны пометить все сообшения ветки как обычные или измененные.
            Для этого выясняем: это родительское сообщение, или имеет такое в поле copy.
            Его и все копированные помечаем и сохраняем. Создаем запись в таблице закрепленных сообщений,
            и в поле copy записываем сообшение, которое открепляем. Мера нужна для показывания людям сообщения,
            которое открепили, чтобы новое поле не создавать, их и так много.
            Также создаем сокеты, чтобы участники чата увидели новое инфо-сообщение сразу
        """
        if self.copy:
            message = self.copy
            if message.type == "_FIX":
                message.type = "PUB"
            else:
                message.type = "EDI"
            message.save(update_fields=['type'])
            for i in Message.objects.filter(copy_id=message.pk):
                if i.type == "_FIX":
                    i.type = "PUB"
                else:
                    i.type = "EDI"
                i.save(update_fields=['type'])
        else:
            if self.type == "_FIX":
                self.type = "PUB"
            else:
                self.type = "EDI"
            self.save(update_fields=['type'])
            for i in Message.objects.filter(copy_id=self.pk):
                if i.type == "_FIX":
                    i.type = "PUB"
                else:
                    i.type = "EDI"
                i.save(update_fields=['type'])

        if MessageFixed.objects.filter(chat_id=self.chat.id,message=self).exists():
            fixed_message = MessageFixed.objects.get(chat_id=self.chat.id,message=self).delete()
            if creator.is_women():
                var = " открепила"
            else:
                var = " открепил"
            text = var + " сообщение "
            info_message = Message.objects.create(chat_id=self.chat.id,creator_id=creator.id,type=Message.MANAGER,text=text,copy=self)
            for recipient in self.chat.get_recipients_2(creator.pk):
                info_message.create_socket(recipient.user.pk, recipient.beep())
            return info_message

    def edit_message(self, text, attach):
        from common.processing.message import get_edit_message_processing

        MessageVersion.objects.create(message=self, text=self.text, attach=self.attach.replace("<div class='attach_container'></div>", ""))
        if self.type == Message.PUBLISHED:
            self.type = Message.EDITED
        elif self.type == Message.FIXED:
            self.type = Message.FIXED_EDITED
        self.attach = self.get_attach(attach)
        self.text = text
        get_edit_message_processing(self)
        self.save()
        for copy in Message.objects.filter(copy_id=self.pk):
            copy.attach = self.attach
            copy.text = self.text
            copy.type = self.type
            copy.save()
        return self

    def get_created(self):
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(self.created)

    def get_text_60(self):
        import re
        count = 60
        images = re.findall(r'<img.*?>', self.text)
        for image in images:
            count += (len(image) -1)
        return self.text[:count].replace("<br>", "  ")

    def get_type_text(self):
        if self.is_have_transfer():
            if self.transfer.all().count() > 1:
                return "Пересланные сообщения"
            else:
                return "Пересланное сообщение"
        elif self.parent:
            return "Ответ на сообщение"
        elif self.sticker:
            return "Стикер"
        elif self.voice:
            return "Голосовое сообщение"
        elif self.attach and self.text:
            return "Текст и вложения"
        elif self.attach and not self.text:
            return "Вложения"
        elif self.text:
            return self.get_text_60()

    def get_preview_text(self):
        text = self.get_type_text()
        if self.is_manager():
            creator = self.creator
            message = self.copy
            return creator.get_full_name() + self.text + '<span class="underline">' + message.get_text_60() + '</span>'
        else:
            return text

    def get_manager_text(self):
        message = self.copy
        text = message.get_type_text()
        return '<i><a target="_blank" href="' + self.creator.get_link() + '">' + self.creator.get_full_name() + '</a><span>' + self.text + '</span><a class="pointer show_selected_fix_message underline">' + text + '</a>' + '</i>'

    def is_repost(self):
        return self.repost

    def is_photo_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.PHOTO_REPOST)
    def get_photo_repost(self):
        photo = self.repost.parent.item_photo.filter(is_deleted=False)[0]
        return photo
    def is_photo_list_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.PHOTO_LIST_REPOST)
    def get_photo_list_repost(self):
        return self.repost.parent.post_list.filter(is_deleted=False)[0]

    def is_music_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.MUSIC_REPOST)
    def is_music_list_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.MUSIC_LIST_REPOST)
    def get_playlist_repost(self):
        playlist = self.repost.parent.post_soundlist.exclude(type__contains="_")[0]
        return playlist
    def get_music_repost(self):
        music = self.repost.parent.item_music.exclude(type__contains="_")[0]
        return music

    def is_good_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.GOOD_REPOST)
    def is_good_list_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.GOOD_LIST_REPOST)
    def get_good_repost(self):
        return self.repost.item_good.exclude(type__contains="_")[0]
    def get_good_list_repost(self):
        return self.repost.parent.post_good_list.exclude(type__contains="_")[0]

    def is_doc_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.DOC_REPOST)
    def is_doc_list_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.DOC_LIST_REPOST)
    def get_doc_list_repost(self):
        return self.repost.parent.post_doclist.exclude(type__contains="_")[0]
    def get_doc_repost(self):
        return self.repost.parent.item_doc.exclude(type__contains="_")[0]

    def is_video_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.VIDEO_REPOST)
    def is_video_list_repost(self):
        from posts.models import Post
        return try_except(self.repost.type == Post.VIDEO_LIST_REPOST)
    def get_video_list_repost(self):
        return self.repost.parent.post_video_list.exclude(type__contains="_")[0]

    def get_u_message_parent(self, user):
        from common.attach.message_attach import get_u_message_parent
        return get_u_message_parent(self.parent, user)

    def get_c_message_parent(self, user):
        from common.attach.message_attach import get_c_message_parent
        return get_c_message_parent(self.parent, user)

    def get_attach(self, user):
        from common.attach.message_attach import get_message_attach
        return get_message_attach(self, user)

    def get_edit_attach(self, user):
        from common.attach.message_attach import get_message_edit
        return get_message_edit(self, user)

    def get_attach_photos(self):
        if "pho" in self.attach:
            query = []
            from gallery.models import Photo

            for item in self.attach.split(","):
                if item[:3] == "pho":
                    query.append(item[3:])
        return Photo.objects.filter(id__in=query)

    def get_attach_videos(self):
        if "vid" in self.attach:
            query = []
            from video.models import Video
            for item in self.attach.split(","):
                if item[:3] == "vid":
                    query.append(item[3:])
        return Video.objects.filter(id__in=query)

    def delete_item(self, community):
        if self.type == "PUB":
            self.type = Message.DELETED
        elif self.type == "EDI":
            self.type = Message.DELETED_EDITED
        elif self.type == "_FIX":
            self.type = Message.DELETED_FIXED
        self.save(update_fields=['type'])
    def restore_item(self, community):
        from notify.models import Notify, Wall
        if self.type == "_DEL":
            self.type = Message.PUBLISHED
        elif self.type == "_DELE":
            self.type = Message.EDITED
        elif self.type == "_DELF":
            self.type = Message.FIXED
        self.save(update_fields=['type'])

    def close_item(self, community):
        if self.type == "PUB":
            self.type = Message.CLOSED
        elif self.type == "EDI":
            self.type = Message.CLOSED_EDITED
        elif self.type == "_FIX":
            self.type = Message.CLOSED_FIXED
        self.save(update_fields=['type'])
    def abort_close_item(self, community):
        if self.type == "_CLO":
            self.type = Message.PUBLISHED
        elif self.type == "_CLOE":
            self.type = Message.EDITED
        elif self.type == "_CLOF":
            self.type = Message.FIXED
        self.save(update_fields=['type'])


class MessageFavourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', verbose_name="Добавивший", null=True, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='+', verbose_name="Сообщение", null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'message'),)
        verbose_name = 'Избранное сообщение'
        verbose_name_plural = 'Избранные сообщения'


class MessageVersion(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="message_version")
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000, blank=True)
    attach = models.CharField(blank=True, max_length=200, verbose_name="Прикрепленные элементы")
    transfer = models.ManyToManyField("self", blank=True, related_name='+')

    class Meta:
        verbose_name = "Копия сообщения перед изменением"
        verbose_name_plural = "Копии сообщений перед изменением"
        ordering = ["-created"]
        indexes = (BrinIndex(fields=['created']),)

    def __str__(self):
        return self.text


class MessageFixed(models.Model):
    chat = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', verbose_name="Чат", on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', verbose_name="Тот, кто закрепил сообщение", null=True, on_delete=models.SET_NULL)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Закрепленное сообщение"
        verbose_name_plural = "Закрепленные сообщения"
        ordering = ["-created"]
        indexes = (BrinIndex(fields=['created']),)

    def __str__(self):
        return self.text

    def get_fixed_message_for_chat(self, chat_id, creator_id,):
        if self.type == "PUB":
            self.type = "_FIX"
        else:
            self.type = "_FIXE"
        self.save(update_fields=['type'])
        fixed_message = MessageFixed.objects.create(chat_id=chat_id,creator_id=creator_id,message=self)
        return fixed_message

    def get_unfixed_message_for_chat(self, chat_id):
        if self.type == "_FIX":
            self.type = "PUB"
        else:
            self.type = "EDI"
        self.save(update_fields=['type'])
        if MessageFixed.objects.filter(chat_id=chat_id,message=self).exists():
            fixed_message = MessageFixed.objects.get(chat_id=chat_id,message=self).delete()

    def get_preview_message(self):
        message = self.message
        if message.is_manager():
            creator = self.creator
            return '<i><a target="_blank" href="' + creator.get_link() + '">' + creator.get_full_name() + '</a>' + message.text + '</i>'
        elif message.is_have_transfer():
            if message.transfer.all().count() > 1:
                return "Пересланные сообщения"
            else:
                return "Пересланное сообщение"
        elif message.parent:
            return "Ответ на сообщение"
        elif message.attach:
            return "Вложения"
        elif message.voice:
            return "Голосовое сообщение"
        elif message.sticker:
            return "Наклейка"
        elif message.text:
            import re
            count = 60
            images = re.findall(r'<img.*?>', message.text)
            for image in images:
                count += (len(image) -1)
            return message.text[:count].replace("<br>", "  ")

    def get_created(self):
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(self.created)


class ChatPerm(models.Model):
    """ связь с таблицей участников беседы. Появляется после ее инициирования, когда участник
        получит какое либо исключение или включение для какой-либо категории.
        1. NO_VALUE - неактивное значение.
        2. YES_ITEM - может соверщать описанные действия
        3. NO_ITEM - не может соверщать описанные действия
    """
    NO_VALUE, YES_ITEM, NO_ITEM = 0, 1, 2
    ITEM = (
        (NO_VALUE, 'Не активно'),
        (YES_ITEM, 'Может иметь действия с элементом'),
        (NO_ITEM, 'Не может иметь действия с элементом'),
    )

    user = models.OneToOneField(Connect, null=True, blank=True, on_delete=models.CASCADE, related_name='connect_settings', verbose_name="Друг")

    can_add_in_chat = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто добавляет в беседы")
    can_add_info = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто редактирует информации")
    can_add_fix = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто закрепляет сообщения")
    can_send_mention = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто отправляет массовые упоминания")
    can_see_post_comment = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто видит комменты к записям")
    can_add_admin = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто добавляет админов и работает с ними")
    can_add_design = models.PositiveSmallIntegerField(choices=ITEM, default=0, verbose_name="Кто меняет дизайн")

    class Meta:
        verbose_name = 'Исключения/Включения участника беседы'
        verbose_name_plural = 'Исключения/Включения участников беседы'
        index_together = [('id', 'user'),]
