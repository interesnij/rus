from django.db import models
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from notifications.models import Notification, notification_handler
from django.utils import timezone
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
import uuid
from django.contrib.contenttypes.fields import GenericRelation



class GoodCategory(models.Model):
	name=models.CharField(max_length=100, verbose_name="Название категории")
	order=models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
	image=models.ImageField(blank=True, verbose_name="Изображение", upload_to="goods/list")

	def __str__(self):
		return self.name

	class Meta:
		ordering=["order","name"]
		verbose_name="категория товаров"
		verbose_name_plural="категории товаров"


class GoodSubCategory(models.Model):
	name=models.CharField(max_length=100, verbose_name="Название подкатегории")
	order=models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер подкатегории")
	category=models.ForeignKey(GoodCategory, on_delete=models.CASCADE, verbose_name="Категория-родитель")
	image=models.ImageField(blank=True, verbose_name="Изображение", upload_to="sub_category/list")

	def __str__(self):
		return self.name

	class Meta:
		ordering=["order","name"]
		verbose_name="Подкатегория товаров"
		verbose_name_plural="Подкатегории товаров"

class Good(models.Model):

	uuid = models.UUIDField(default=uuid.uuid4, db_index=True,verbose_name="uuid")
	title = models.CharField(max_length=200, verbose_name="Название")
	sub_category = models.ForeignKey(GoodSubCategory, on_delete=models.CASCADE, verbose_name="Подкатегория")
	price = models.PositiveIntegerField(default=0, verbose_name="Цена товара")
	description = models.TextField(max_length=1000, verbose_name="Описание товара")
	community = models.ForeignKey('communities.Community', db_index=False, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Сообщество")
	comments_enabled = models.BooleanField(default=True, verbose_name="Разрешить комментарии")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, verbose_name="Создатель")
	is_deleted = models.BooleanField(default=False, verbose_name="Удалено")
	views=models.IntegerField(default=0, verbose_name="Просмотры")
	moderated_object = GenericRelation('moderation.ModeratedObject', related_query_name='goods')

	image = ProcessedImageField(verbose_name='Главное изображение', format='JPEG',options={'quality': 80}, processors=[ResizeToFit(512,512)],upload_to="goods/%Y/%m/%d")
	image2 = ProcessedImageField(verbose_name='изображение 2', blank=True, format='JPEG',options={'quality': 80}, processors=[ResizeToFill(512, 512)],upload_to="goods/%Y/%m/%d")
	image3 = ProcessedImageField(verbose_name='изображение 3', blank=True, format='JPEG',options={'quality': 80}, processors=[ResizeToFit(512, 512)],upload_to="goods/%Y/%m/%d")
	image4 = ProcessedImageField(verbose_name='изображение 4', blank=True, format='JPEG',options={'quality': 80}, processors=[ResizeToFit(512, 512)],upload_to="goods/%Y/%m/%d")
	image5 = ProcessedImageField(verbose_name='изображение 5', blank=True, format='JPEG',options={'quality': 80}, processors=[ResizeToFit(512, 512)],upload_to="goods/%Y/%m/%d")

	STATUS_DRAFT = 'D'
	STATUS_SOLD = 'S'
	STATUS_PUBLISHED = 'P'
	STATUSES = (
		(STATUS_DRAFT, 'Отложен'),
		(STATUS_PUBLISHED, 'Опубликован'),
		(STATUS_SOLD, 'Продан'),
		)
	status = models.CharField(blank=False, null=False, choices=STATUSES, default=STATUS_PUBLISHED, max_length=2, verbose_name="Статус")

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		channel_layer = get_channel_layer()
		payload = {"type": "receive","key": "additional_post","actor_name": self.creator.get_full_name()}
		async_to_sync(channel_layer.group_send)('notifications', payload)

	class Meta:
		indexes = (BrinIndex(fields=['created']),)
		verbose_name="Товар"
		verbose_name_plural="Товары"
