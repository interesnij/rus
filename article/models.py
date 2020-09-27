from django.db import models
import uuid
from pilkit.processors import ResizeToFit, ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from imagekit.models import ProcessedImageField
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.postgres.indexes import BrinIndex
from django.utils import timezone


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Заголовок" )
    g_image = ProcessedImageField(verbose_name='Главное изображение', blank=False, format='JPEG',options={'quality': 80}, processors=[ResizeToFill(1024, 700)],upload_to='articles/%Y/%m/%d')
    content = RichTextUploadingField(config_name='default',external_plugin_resources=[('youtube','/static/ckeditor_plugins/youtube/youtube/','plugin.js',)],)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True,verbose_name="uuid")
    community = models.ForeignKey('communities.Community', db_index=False, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Сообщество")
    created = models.DateTimeField(default=timezone.now, verbose_name="Создан")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, related_name='article_creator', on_delete=models.CASCADE, verbose_name="Создатель")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалено")
    STATUS_DRAFT = 'D'
    STATUS_PROCESSING = 'PG'
    STATUS_PUBLISHED = 'P'
    STATUS_ARHIVED = 'A'
    STATUSES = (
        (STATUS_DRAFT, 'Черновик'),
        (STATUS_PROCESSING, 'Обработка'),
        (STATUS_PUBLISHED, 'Опубликована'),
        (STATUS_ARHIVED, 'Архивирована'),
    )
    status = models.CharField(blank=False, null=False, choices=STATUSES, default=STATUS_PUBLISHED, max_length=2, verbose_name="Статус статьи")

    post = models.ManyToManyField("posts.Post", blank=True, related_name='attached_item')
    comment_attach = models.ManyToManyField("posts.PostComment", blank=True, related_name='attached_comment')
    message = models.ManyToManyField('chat.Message', blank=True, related_name='attached_message')

    @classmethod
    def create_article(cls, creator, title, community, g_image, content, created, status ):
        article = Article.objects.create(creator=creator,content=content,g_image=g_image,community=community,title=title)

        channel_layer = get_channel_layer()
        payload = {
                "type": "receive",
                "key": "additional_post",
                "actor_name": article.creator.get_full_name()
            }
        async_to_sync(channel_layer.group_send)('notifications', payload)
        return article

    def get_created(self):
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(self.created)

    class Meta:
        ordering = ["-created"]
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        indexes = (BrinIndex(fields=['created']),)

    def __str__(self):
        return self.title
