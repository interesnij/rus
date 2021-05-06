from django.db import models
import uuid
from pilkit.processors import ResizeToFill, ResizeToFit, Transpose
from imagekit.models import ProcessedImageField
from django.conf import settings
from django.contrib.postgres.indexes import BrinIndex
from django.db.models import Q
from goods.helpers import upload_to_good_directory
from django.db.models.signals import post_save
from django.dispatch import receiver
from communities.models import Community


class GoodCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название категории")
	order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
	image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="goods/list")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["order","name"]
		verbose_name = "категория товаров"
		verbose_name_plural = "категории товаров"


class GoodSubCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название подкатегории")
	order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер подкатегории")
	category = models.ForeignKey(GoodCategory, on_delete=models.CASCADE, verbose_name="Категория-родитель")
	image = models.ImageField(blank=True, verbose_name="Изображение", upload_to="goods/list")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["order","name"]
		verbose_name = "Подкатегория товаров"
		verbose_name_plural = "Подкатегории товаров"


class GoodList(models.Model):
	MAIN, LIST, MANAGER, THIS_PROCESSING, PRIVATE = 'MAI', 'LIS', 'MAN', '_PRO', 'PRI'
	THIS_DELETED, THIS_DELETED_PRIVATE, THIS_DELETED_MANAGER = '_DEL', '_DELP', '_DELM'
	THIS_CLOSED, THIS_CLOSED_PRIVATE, THIS_CLOSED_MAIN, THIS_CLOSED_MANAGER = '_CLO', '_CLOP', '_CLOM', '_CLOMA'
	TYPE = (
		(MAIN, 'Основной'),(LIST, 'Пользовательский'),(PRIVATE, 'Приватный'),(MANAGER, 'Созданный персоналом'),(THIS_PROCESSING, 'Обработка'),
		(THIS_DELETED, 'Удалённый'),(THIS_DELETED_PRIVATE, 'Удалённый приватный'),(THIS_DELETED_MANAGER, 'Удалённый менеджерский'),
		(THIS_CLOSED, 'Закрытый менеджером'),(THIS_CLOSED_PRIVATE, 'Закрытый приватный'),(THIS_CLOSED_MAIN, 'Закрытый основной'),(THIS_CLOSED_MANAGER, 'Закрытый менеджерский'),
		)
	community = models.ForeignKey('communities.Community', related_name='good_lists_community', db_index=False, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Сообщество")
	uuid = models.UUIDField(default=uuid.uuid4, verbose_name="uuid")
	name = models.CharField(max_length=250, verbose_name="Название")
	type = models.CharField(max_length=6, choices=TYPE, default=THIS_PROCESSING, verbose_name="Тип альбома")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	order = models.PositiveIntegerField(default=0)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='good_list_creator', verbose_name="Создатель")
	description = models.CharField(max_length=200, blank=True, verbose_name="Описание")

	users = models.ManyToManyField("users.User", blank=True, related_name='+')
	communities = models.ManyToManyField('communities.Community', blank=True, related_name='+')

	class Meta:
		indexes = (BrinIndex(fields=['created']),)
		verbose_name = 'Подборка товаров'
		verbose_name_plural = 'Подборки товаров'

	def __str__(self):
		return self.name

	@receiver(post_save, sender=Community)
	def create_c_model(sender, instance, created, **kwargs):
		if created:
			GoodList.objects.create(community=instance, type=GoodList.MAIN, name="Основной список", order=0, creator=instance.creator)
	@receiver(post_save, sender=settings.AUTH_USER_MODEL)
	def create_u_model(sender, instance, created, **kwargs):
		if created:
			GoodList.objects.create(creator=instance, type=GoodList.MAIN, name="Основной список", order=0)

	def is_main(self):
		return self.type == self.MAIN
	def is_list(self):
		return self.type == self.LIST
	def is_private(self):
		return self.type == self.PRIVATE
	def is_open(self):
		return self.type[0] != "_"

	def get_items(self):
		return self.good_list.filter(status="PUB")
	def get_staff_items(self):
		return self.good_list.filter(Q(status="PUB")|Q(status="PRI"))
	def count_items(self):
		try:
			return self.good_list.filter(status="PUB").values("pk").count()
		except:
			return 0
	def count_items_ru(self):
		count = self.count_items()
		a, b = count % 10, count % 100
		if (a == 1) and (b != 11):
			return str(count) + " товар"
		elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
			return str(count) + " товара"
		else:
			return str(count) + " товаров"

	def is_not_empty(self):
		 return self.good_list.filter(status="PUB").values("pk").exists()
	def get_users_ids(self):
		users = self.users.exclude(type__contains="_").values("pk")
		return [i['pk'] for i in users]
	def get_communities_ids(self):
		communities = self.communities.exclude(type__contains="_").values("pk")
		return [i['pk'] for i in communities]

	def is_user_can_add_list(self, user_id):
		return self.creator.pk != user_id and user_id not in self.get_users_ids()
	def is_user_can_delete_list(self, user_id):
		return self.creator.pk != user_id and user_id in self.get_users_ids()

	def is_community_can_add_list(self, community_id):
		return self.community.pk != community_id and community_id not in self.get_communities_ids()
	def is_community_can_delete_list(self, community_id):
		return self.community.pk != community_id and community_id in self.get_communities_ids()

	def get_cover(self):
		if self.image:
			return self.image.url
		else:
			return '/static/images/no_img/list.jpg'

	@classmethod
	def get_user_staff_lists(cls, user_pk):
		query = Q(creator_id=user_pk, community__isnull=True)|Q(users__id=user_pk)
		query.add(~Q(Q(type__contains="_")|Q(type="MAI")), Q.AND)
		return cls.objects.filter(query)
	@classmethod
	def is_have_user_staff_lists(cls, user_pk):
		query = Q(creator_id=user_pk, community__isnull=True)|Q(users__id=user_pk)
		query.add(~Q(Q(type__contains="_")|Q(type="MAI")), Q.AND)
		return cls.objects.filter(query).exists()
	@classmethod
	def get_user_lists(cls, user_pk):
		query = Q(creator_id=user_pk, community__isnull=True)|Q(users__id=user_pk)
		query.add(Q(type="LIS"), Q.AND)
		return cls.objects.filter(query).order_by("order")
	@classmethod
	def is_have_user_lists(cls, user_pk):
		query = Q(creator_id=user_pk, community__isnull=True)|Q(users__id=user_pk)
		query.add(Q(type="LIS"), Q.AND)
		return cls.objects.filter(query).exists()
	@classmethod
	def get_user_lists_count(cls, user_pk):
		query = Q(creator_id=user_pk, community__isnull=True)|Q(users__id=user_pk)
		query.add(Q(type="LIS"), Q.AND)
		return cls.objects.filter(query).values("pk").count()

	@classmethod
	def get_community_staff_lists(cls, community_pk):
		query = Q(community_id=user_pk)|Q(communities__id=user_pk)
		query.add(~Q(Q(type__contains="_")|Q(type="MAI")), Q.AND)
		return cls.objects.filter(query)
	@classmethod
	def is_have_community_staff_lists(cls, community_pk):
		query = Q(community_id=user_pk)|Q(communities__id=user_pk)
		query.add(~Q(Q(type__contains="_")|Q(type="MAI")), Q.AND)
		return cls.objects.filter(query).exists()
	@classmethod
	def get_community_lists(cls, community_pk):
		query = Q(community_id=user_pk)|Q(communities__id=user_pk)
		query.add(Q(type="LIS"), Q.AND)
		return cls.objects.filter(query).order_by("order")
	@classmethod
	def is_have_community_lists(cls, community_pk):
		query = Q(community_id=user_pk)|Q(communities__id=user_pk)
		query.add(Q(type="LIS"), Q.AND)
		return cls.objects.filter(query).exists()
	@classmethod
	def get_community_lists_count(cls, community_pk):
		query = Q(community_id=user_pk)|Q(communities__id=user_pk)
		query.add(Q(type="LIS"), Q.AND)
		return cls.objects.filter(query).values("pk").count()

	@classmethod
	def create_list(cls, creator, name, description, order, community, is_public):
		from notify.models import Notify, Wall
		from common.processing.good import get_good_list_processing
		if not order:
			order = 1
		if community:
			list = cls.objects.create(creator=creator,name=name,description=description, order=order, community=community)
			get_good_list_processing(list, GoodList.LIST)
			if is_public:
				from common.notify.progs import community_send_notify, community_send_wall
				Wall.objects.create(creator_id=creator.pk, community_id=community.pk, recipient_id=user_id, type="GOL", object_id=list.pk, verb="ITE")
				community_send_wall(list.pk, creator.pk, community.pk, None, "create_c_good_list_wall")
				for user_id in community.get_member_for_notify_ids():
					Notify.objects.create(creator_id=creator.pk, community_id=community.pk, recipient_id=user_id, type="GOL", object_id=list.pk, verb="ITE")
					community_send_notify(list.pk, creator.pk, user_id, community.pk, None, "create_c_good_list_notify")
		else:
			list = cls.objects.create(creator=creator,name=name,description=description, order=order)
			get_good_list_processing(list, GoodList.LIST)
			if is_public:
				from common.notify.progs import user_send_notify, user_send_wall
				Wall.objects.create(creator_id=creator.pk, type="GOL", object_id=list.pk, verb="ITE")
				user_send_wall(list.pk, None, "create_u_good_list_wall")
				for user_id in creator.get_user_news_notify_ids():
					Notify.objects.create(creator_id=creator.pk, recipient_id=user_id, type="GOL", object_id=list.pk, verb="ITE")
					user_send_notify(list.pk, creator.pk, user_id, None, "create_u_good_list_notify")
		return list
	def edit_list(self, name, description, order, is_public):
		from common.processing.good import get_good_list_processing
		if not order:
			order = 1
		self.name = name
		self.description = description
		self.order = order
		self.save()
		if is_public:
			get_good_list_processing(self, GoodList.LIST)
			self.make_publish()
		else:
			get_good_list_processing(self, GoodList.PRIVATE)
			self.make_private()
		return self

	def make_private(self):
		from notify.models import Notify, Wall
		self.type = GoodList.PRIVATE
		self.save(update_fields=['type'])
		if Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="C")
		if Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="C")
	def make_publish(self):
		from notify.models import Notify, Wall
		self.type = GoodList.LIST
		self.save(update_fields=['type'])
		if Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="R")
		if Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="R")
	def delete_list(self):
		from notify.models import Notify, Wall
		if self.type == "LIS":
			self.type = GoodList.THIS_DELETED
		elif self.type == "PRI":
			self.type = GoodList.THIS_DELETED_PRIVATE
		elif self.type == "MAN":
			self.type = GoodList.THIS_DELETED_MANAGER
		self.save(update_fields=['type'])
		if Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="C")
		if Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="C")
	def restore_list(self):
		from notify.models import Notify, Wall
		if self.type == "_DEL":
			self.type = GoodList.LIST
		elif self.type == "_DELP":
			self.type = GoodList.PRIVATE
		elif self.type == "_DELM":
			self.type = GoodList.MANAGER
		self.save(update_fields=['type'])
		if Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="R")
		if Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="R")

	def close_item(self):
		from notify.models import Notify, Wall
		if self.type == "LIS":
			self.type = GoodList.THIS_CLOSED
		elif self.type == "MAI":
			self.type = GoodList.THIS_CLOSED_MAIN
		elif self.type == "PRI":
			self.type = GoodList.THIS_CLOSED_PRIVATE
		elif self.type == "MAN":
			self.type = GoodList.THIS_CLOSED_MANAGER
		self.save(update_fields=['type'])
		if Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="C")
		if Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="C")
	def abort_close_item(self):
		from notify.models import Notify, Wall
		if self.type == "_CLO":
			self.type = GoodList.LIST
		elif self.type == "_CLOM":
			self.type = GoodList.MAIN
		elif self.type == "_CLOP":
			self.type = GoodList.PRIVATE
		elif self.type == "_CLOM":
			self.type = GoodList.MANAGER
		self.save(update_fields=['type'])
		if Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="R")
		if Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOL", object_id=self.pk, verb="ITE").update(status="R")


class Good(models.Model):
	THIS_PROCESSING, THIS_DRAFT, PUBLISHED, PRIVATE, MANAGER, THIS_DELETED, THIS_CLOSED = '_PRO', '_DRA','PUB','PRI','MAN','_DEL','_CLO'
	THIS_DELETED_PRIVATE, THIS_DELETED_MANAGER, THIS_CLOSED_PRIVATE, THIS_CLOSED_MANAGER = '_DELP','_DELM','_CLOP','_CLOM'
	STATUS = (
		(THIS_PROCESSING, 'Обработка'),(THIS_DRAFT, 'Черновик'),(PUBLISHED, 'Опубликовано'),(THIS_DELETED, 'Удалено'),(PRIVATE, 'Приватно'),(THIS_CLOSED, 'Закрыто модератором'),(MANAGER, 'Созданный персоналом'),
		(THIS_DELETED_PRIVATE, 'Удалённый приватный'),(THIS_DELETED_MANAGER, 'Удалённый менеджерский'),(THIS_CLOSED_PRIVATE, 'Закрытый приватный'),(THIS_CLOSED_MANAGER, 'Закрытый менеджерский'),
	)
	title = models.CharField(max_length=200, verbose_name="Название")
	sub_category = models.ForeignKey(GoodSubCategory, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Подкатегория")
	price = models.PositiveIntegerField(default=0, blank=True, verbose_name="Цена товара")
	description = models.TextField(max_length=1000, verbose_name="Описание товара")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="good_creator", on_delete=models.CASCADE, verbose_name="Создатель")
	image = ProcessedImageField(verbose_name='Главное изображение', blank=True, format='JPEG',options={'quality': 80}, processors=[Transpose(), ResizeToFit(512,512)],upload_to=upload_to_good_directory)
	status = models.CharField(choices=STATUS, default=THIS_PROCESSING, max_length=6, verbose_name="Статус")

	comments_enabled = models.BooleanField(default=True, verbose_name="Разрешить комментарии")
	votes_on = models.BooleanField(default=True, verbose_name="Реакции разрешены")
	list = models.ManyToManyField(GoodList, related_name="good_list", blank=True)

	comment = models.PositiveIntegerField(default=0, verbose_name="Кол-во комментов")
	view = models.PositiveIntegerField(default=0, verbose_name="Кол-во просмотров")
	ad_view = models.PositiveIntegerField(default=0, verbose_name="Кол-во рекламных просмотров")
	like = models.PositiveIntegerField(default=0, verbose_name="Кол-во лайков")
	dislike = models.PositiveIntegerField(default=0, verbose_name="Кол-во дизлайков")
	repost = models.PositiveIntegerField(default=0, verbose_name="Кол-во репостов")

	def __str__(self):
		return self.title

	class Meta:
		indexes = (BrinIndex(fields=['created']),)
		verbose_name="Товар"
		verbose_name_plural="Товары"
		ordering = ["-created"]

	def get_created(self):
		from django.contrib.humanize.templatetags.humanize import naturaltime
		return naturaltime(self.created)

	def plus_comments(self, count):
		self.comment += count
		return self.save(update_fields=['comment'])
	def minus_comments(self, count):
		self.comment -= count
		return self.save(update_fields=['comment'])
	def plus_views(self, count):
		self.view += count
		return self.save(update_fields=['view'])
	def minus_views(self, count):
		self.view -= count
		return self.save(update_fields=['view'])
	def plus_reposts(self, count):
		self.repost += count
		return self.save(update_fields=['repost'])
	def minus_reposts(self, count):
		self.repost -= count
		return self.save(update_fields=['repost'])

	def likes(self):
		return GoodVotes.objects.filter(parent=self, vote__gt=0)

	def is_draft(self):
		if self.status == Good.DRAFT:
			return True
		else:
			return False

	def likes_count(self):
		if self.like > 0:
			return self.like
		else:
			return ''

	def window_likes(self):
		from common.model.votes import GoodVotes
		return GoodVotes.objects.filter(parent=self, vote__gt=0)[0:6]

	def dislikes(self):
		from common.model.votes import GoodVotes
		return GoodVotes.objects.filter(parent=self, vote__lt=0)

	def dislikes_count(self):
		if self.dislike > 0:
			return self.dislike
		else:
			return ''

	def window_dislikes(self):
		from common.model.votes import GoodVotes
		return GoodVotes.objects.filter(parent=self, vote__lt=0)[0:6]

	def get_reposts(self):
		return Good.objects.filter(parent=self)

	def get_window_reposts(self):
		return Good.objects.filter(parent=self)[0:6]

	def count_reposts(self):
		if self.repost > 0:
			return self.repost
		else:
			return ''

	def get_comments(self):
		comments_query = Q(good_id=self.pk)
		comments_query.add(Q(parent__isnull=True), Q.AND)
		return GoodComment.objects.filter(comments_query)
	def count_comments(self):
		if self.comment > 0:
			return self.comment
		else:
			return ''

	def all_visits_count(self):
		from stst.models import GoodNumbers

		count = GoodNumbers.objects.filter(good=self.pk).values('pk').count()
		a = count % 10
		b = count % 100
		if (a == 1) and (b != 11):
			return str(count) + " просмотр"
		elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
			return str(count) + " просмотра"
		else:
			return str(count) + " просмотров"

	def visits_count(self):
		from stst.models import GoodNumbers
		return GoodNumbers.objects.filter(good=self.pk).values('pk').count()

	def get_lists_for_good(self):
		return self.list.all()

	def get_list_uuid(self):
		return self.list.all()[0].uuid

	def get_images(self):
		return GoodImage.objects.filter(good_id=self.pk)

	@classmethod
	def create_good(cls, creator, description, votes_on, comments_enabled, title, image, images, price, lists, sub_category, community, is_public):
		from common.processing.good import get_good_processing
		if not lists:
			from rest_framework.exceptions import ValidationError
			raise ValidationError("Не выбран список для нового Товара")
		private = 0
		if not price:
			price = 0
		good = cls.objects.create(creator=creator,title=title,description=description,votes_on=votes_on,comments_enabled=comments_enabled,image=image,price=price,sub_category=sub_category,community=community)
		for img in images:
			GoodImage.objects.create(good=good, image=img)
		for list_id in lists:
			good_list = GoodList.objects.get(pk=list_id)
			good_list.good_list.add(good)
			if good_list.is_private():
				private = 1
		if not private and is_public:
			get_good_processing(good, Good.PUBLISHED)
			if community:
				from common.notify.progs import community_send_notify, community_send_wall
				from notify.models import Notify, Wall

				Wall.objects.create(creator_id=creator.pk, community_id=community.pk, recipient_id=user_id, type="GOO", object_id=good.pk, verb="ITE")
				community_send_wall(good.pk, creator.pk, community.pk, None, "create_c_good_wall")
				for user_id in community.get_member_for_notify_ids():
					Notify.objects.create(creator_id=creator.pk, community_id=community.pk, recipient_id=user_id, type="GOO", object_id=good.pk, verb="ITE")
					community_send_notify(good.pk, creator.pk, user_id, community.pk, None, "create_c_good_notify")
			else:
				from common.notify.progs import user_send_notify, user_send_wall
				from notify.models import Notify, Wall

				Wall.objects.create(creator_id=creator.pk, type="GOO", object_id=good.pk, verb="ITE")
				user_send_wall(good.pk, None, "create_u_good_wall")
				for user_id in creator.get_user_news_notify_ids():
					Notify.objects.create(creator_id=creator.pk, recipient_id=user_id, type="GOO", object_id=good.pk, verb="ITE")
					user_send_notify(good.pk, creator.pk, user_id, None, "create_u_good_notify")
		else:
			get_good_processing(good, Good.PRIVATE)
			return good

	def edit_good(self, description, votes_on, comments_enabled, title, image, images, price, lists, sub_category, is_public):
		from common.processing.good import get_good_processing
		self.title = title
		self.description = description
		self.lists = lists
		self.votes_on = votes_on
		self.comments_enabled = comments_enabled
		self.image = image
		self.price = price
		self.sub_category = sub_category
		self.community = community
		if is_public:
			get_good_processing(self, Good.PUBLISHED)
			self.make_publish()
		else:
			get_good_processing(self, Good.PRIVATE)
			self.make_private()
		if images:
			for image in images:
				GoodImage.objects.create(good=good, image=image)
		return self.save()

	def make_private(self):
		from notify.models import Notify, Wall
		self.status = Good.PRIVATE
		self.save(update_fields=['status'])
		if Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="C")
		if Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="C")
	def make_publish(self):
		from notify.models import Notify, Wall
		self.status = Good.PUBLISHED
		self.save(update_fields=['status'])
		if Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="R")
		if Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="R")

	def delete_good(self, community):
		from notify.models import Notify, Wall
		if self.status == "PUB":
			self.status = Good.THIS_DELETED
		elif self.status == "PRI":
			self.status = Good.THIS_DELETED_PRIVATE
		elif self.status == "MAN":
			self.status = Good.THIS_DELETED_MANAGER
		self.save(update_fields=['status'])
		if community:
			community.minus_goods(1)
		else:
			self.creator.minus_goods(1)
		if Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="C")
		if Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="C")
	def restore_good(self, community):
		from notify.models import Notify, Wall
		if self.status == "_DEL":
			self.status = Good.PUBLISHED
		elif self.status == "_DELP":
			self.status = Good.PRIVATE
		elif self.status == "_DELM":
			self.status = Good.MANAGER
		self.save(update_fields=['status'])
		if community:
			community.plus_goods(1)
		else:
			self.creator.plus_goods(1)
		if Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="R")
		if Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="R")

	def close_item(self, community):
		from notify.models import Notify, Wall
		if self.status == "PUB":
			self.status = Good.THIS_CLOSED
		elif self.status == "PRI":
			self.status = Good.THIS_CLOSED_PRIVATE
		elif self.status == "MAN":
			self.status = Good.THIS_CLOSED_MANAGER
		self.save(update_fields=['status'])
		if community:
			community.minus_goods(1)
		else:
			self.creator.minus_goods(1)
		if Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="C")
		if Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="C")
	def abort_close_item(self, community):
		from notify.models import Notify, Wall
		if self.status == "_CLO":
			self.status = Good.PUBLISHED
		elif self.status == "_CLOP":
			self.status = Good.PRIVATE
		elif self.status == "_CLOM":
			self.status = Good.MANAGER
		self.save(update_fields=['status'])
		if community:
			community.plus_goods(1)
		else:
			self.creator.plus_goods(1)
		if Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Notify.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="R")
		if Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").exists():
			Wall.objects.filter(type="GOO", object_id=self.pk, verb="ITE").update(status="R")

	def send_like(self, user, community):
		import json
		from common.model.votes import GoodVotes
		from django.http import HttpResponse
		from common.notify.notify import user_notify, user_wall
		if not self.votes_on:
			from django.http import Http404
			raise Http404
		try:
			item = GoodVotes.objects.get(parent=self, user=user)
			if item.vote != GoodVotes.LIKE:
				item.vote = GoodVotes.LIKE
				item.save(update_fields=['vote'])
				self.like += 1
				self.dislike -= 1
				self.save(update_fields=['like', 'dislike'])
			else:
				item.delete()
				self.like -= 1
				self.save(update_fields=['like'])
		except GoodVotes.DoesNotExist:
			GoodVotes.objects.create(parent=self, user=user, vote=GoodVotes.LIKE)
			self.like += 1
			self.save(update_fields=['like'])
			if community:
				from common.notify.notify import community_notify, community_wall
				community_notify(user, community, None, self.pk, "GOO", "u_good_notify", "LIK")
				community_wall(user, community, None, self.pk, "GOO", "u_good_notify", "LIK")
			else:
				from common.notify.notify import user_notify, user_wall
				user_notify(user, None, self.pk, "GOO", "u_good_notify", "LIK")
				user_wall(user, None, self.pk, "GOO", "u_good_notify", "LIK")
		return HttpResponse(json.dumps({"like_count": str(self.likes_count()),"dislike_count": str(self.dislikes_count())}),content_type="application/json")
	def send_dislike(self, user, community):
		import json
		from common.model.votes import GoodVotes
		from django.http import HttpResponse
		from common.notify.notify import user_notify, user_wall
		if not self.votes_on:
			from django.http import Http404
			raise Http404
		try:
			item = GoodVotes.objects.get(parent=self, user=user)
			if item.vote != GoodVotes.DISLIKE:
				item.vote = GoodVotes.DISLIKE
				item.save(update_fields=['vote'])
				self.like -= 1
				self.dislike += 1
				self.save(update_fields=['like', 'dislike'])
			else:
				item.delete()
				self.dislike -= 1
				self.save(update_fields=['dislike'])
		except GoodVotes.DoesNotExist:
			GoodVotes.objects.create(parent=self, user=user, vote=GoodVotes.DISLIKE)
			self.dislike += 1
			self.save(update_fields=['dislike'])
			if community:
				from common.notify.notify import community_notify, community_wall
				community_notify(user, community, None, self.pk, "GOO", "u_good_notify", "DIS")
				community_wall(user, community, None, self.pk, "GOO", "u_good_notify", "DIS")
			else:
				from common.notify.notify import user_notify, user_wall
				user_notify(user, None, self.pk, "GOO", "u_good_notify", "DIS")
				user_wall(user, None, self.pk, "GOO", "u_good_notify", "DIS")
		return HttpResponse(json.dumps({"like_count": str(self.likes_count()),"dislike_count": str(self.dislikes_count())}),content_type="application/json")


class GoodImage(models.Model):
	good = models.ForeignKey(Good, on_delete=models.CASCADE, null=True)
	image = ProcessedImageField(verbose_name='Изображение', format='JPEG',options={'quality': 100}, processors=[Transpose(), ResizeToFit(1000,1000)],upload_to=upload_to_good_directory)

	def __str__(self):
		return str(self.pk)


class GoodComment(models.Model):
	EDITED, PUBLISHED, THIS_PROCESSING = 'EDI', 'PUB', '_PRO'
	THIS_DELETED, THIS_EDITED_DELETED = '_DEL', '_DELE'
	THIS_CLOSED, THIS_EDITED_CLOSED = '_CLO', '_CLOE'
	STATUS = (
	(PUBLISHED, 'Опубликовано'),(EDITED, 'Изменённый'),(THIS_PROCESSING, 'Обработка'),
		(THIS_DELETED, 'Удалённый'), (THIS_EDITED_DELETED, 'Удалённый изменённый'),
		(THIS_CLOSED, 'Закрытый менеджером'), (THIS_EDITED_CLOSED, 'Закрытый изменённый'),
	)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='good_comment_replies', null=True, blank=True, verbose_name="Родительский комментарий")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Комментатор")
	text = models.TextField(blank=True,null=True)
	comment = models.ForeignKey(Good, on_delete=models.CASCADE, null=True)
	attach = models.CharField(blank=True, max_length=200, verbose_name="Прикрепленные элементы")
	status = models.CharField(max_length=5, choices=STATUS, default=THIS_PROCESSING, verbose_name="Тип альбома")

	like = models.PositiveIntegerField(default=0, verbose_name="Кол-во лайков")
	dislike = models.PositiveIntegerField(default=0, verbose_name="Кол-во дизлайков")
	repost = models.PositiveIntegerField(default=0, verbose_name="Кол-во репостов")

	class Meta:
		indexes = (BrinIndex(fields=['created']), )
		verbose_name = "комментарий к записи"
		verbose_name_plural = "комментарии к записи"

	def __str__(self):
		return "{0}/{1}".format(self.commenter.get_full_name(), self.text[:10])

	def get_replies(self):
		return self.good_comment_replies.filter(Q(status=GoodComment.EDITED)|Q(status=GoodComment.PUBLISHED)).all()

	def count_replies(self):
		return self.get_replies().values("pk").count()

	def likes(self):
		from common.model.votes import GoodCommentVotes
		return GoodCommentVotes.objects.filter(item_id=self.pk, vote__gt=0)

	def window_likes(self):
		from common.model.votes import GoodCommentVotes
		return GoodCommentVotes.objects.filter(item_id=self.pk, vote__gt=0)[0:6]

	def dislikes(self):
		from common.model.votes import GoodCommentVotes
		return GoodCommentVotes.objects.filter(item_id=self.pk, vote__lt=0)

	def window_dislikes(self):
		from common.model.votes import GoodCommentVotes
		return GoodCommentVotes.objects.filter(item_id=self.pk, vote__lt=0)[0:6]

	def likes_count(self):
		if self.like > 0:
			return self.like
		else:
			return ''

	def dislikes_count(self):
		if self.dislike > 0:
			return self.dislike
		else:
			return ''

	def reposts_count(self):
		if self.repost > 0:
			return self.repost
		else:
			return ''

	@classmethod
	def create_comment(cls, commenter, attach, good, parent, text, community):
		from common.notify.notify import community_wall, community_notify, user_wall, user_notify
		from django.utils import timezone

		_attach = str(attach)
		_attach = _attach.replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
		comment = GoodComment.objects.create(commenter=commenter, attach=_attach, parent=parent, good=good, text=text, created=timezone.now())
		good.comment += 1
		good.save(update_fields=["comment"])
		if comment.parent:
			if community:
				community_notify(comment.commenter, community, None, comment.pk, "GOOC", "u_good_comment_notify", "REP")
				community_wall(comment.commenter, community, None, comment.pk, "GOOC", "u_good_comment_notify", "REP")
			else:
				user_notify(comment.commenter, None, comment.pk, "GOOC", "u_good_comment_notify", "REP")
				user_wall(comment.commenter, None, comment.pk, "GOOC", "u_good_comment_notify", "REP")
		else:
			if comment.good.community:
				community_notify(comment.commenter, community, None, comment.pk, "GOOC", "u_good_comment_notify", "COM")
				community_wall(comment.commenter, community, None, comment.pk, "GOOC", "u_good_comment_notify", "COM")
			else:
				user_notify(comment.commenter, None, comment.pk, "GOOC", "u_good_comment_notify", "COM")
				user_wall(comment.commenter, None, comment.pk, "GOOC", "u_good_comment_notify", "COM")
		return comment

	def get_created(self):
		from django.contrib.humanize.templatetags.humanize import naturaltime
		return naturaltime(self.created)

	def count_replies_ru(self):
		count = self.good_comment_replies.filter(is_deleted=False).values("pk").count()
		a = count % 10
		b = count % 100
		if (a == 1) and (b != 11):
			return str(count) + " ответ"
		elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
			return str(count) + " ответа"
		else:
			return str(count) + " ответов"

	def get_u_attach(self, user):
		from common.attach.comment_attach import get_u_comment_attach
		return get_u_comment_attach(self, user)

	def get_c_attach(self, user):
		from common.attach.comment_attach import get_c_comment_attach
		return get_c_comment_attach(self, user)

	def send_like(self, user, community):
		import json
		from common.model.votes import GoodCommentVotes
		from django.http import HttpResponse
		from common.notify.notify import user_notify, user_wall
		try:
			item = GoodCommentVotes.objects.get(item=self, user=user)
			if item.vote != GoodCommentVotes.LIKE:
				item.vote = GoodCommentVotes.LIKE
				item.save(update_fields=['vote'])
				self.like += 1
				self.dislike -= 1
				self.save(update_fields=['like', 'dislike'])
			else:
				item.delete()
				self.like -= 1
				self.save(update_fields=['like'])
		except GoodCommentVotes.DoesNotExist:
			GoodCommentVotes.objects.create(item=self, user=user, vote=GoodCommentVotes.LIKE)
			self.like += 1
			self.save(update_fields=['like'])
			if self.parent:
				if community:
					from common.notify.notify import community_notify, community_wall
					community_notify(user, community, None, self.pk, "GOOC", "u_good_comment_notify", "LRE")
					community_wall(user, community, None, self.pk, "GOOC", "u_good_comment_notify", "LCO")
				else:
					from common.notify.notify import user_notify, user_wall
					user_notify(user, None, self.pk, "GOOC", "u_good_notify", "LRE")
					user_wall(user, None, self.pk, "GOOC", "u_good_notify", "LCO")
			else:
				if community:
					from common.notify.notify import community_notify, community_wall
					community_notify(user, community, None, self.pk, "GOOC", "u_good_comment_notify", "LCO")
					community_wall(user, community, None, self.pk, "GOOC", "u_good_comment_notify", "LCO")
				else:
					from common.notify.notify import user_notify, user_wall
					user_notify(user, None, self.pk, "GOOC", "u_good_comment_notify", "LCO")
					user_wall(user, None, self.pk, "GOOC", "u_good_comment_notify", "LCO")
		return HttpResponse(json.dumps({"like_count": str(self.likes_count()),"dislike_count": str(self.dislikes_count())}),content_type="application/json")
	def send_dislike(self, user, community):
		import json
		from common.model.votes import GoodCommentVotes
		from django.http import HttpResponse
		from common.notify.notify import user_notify, user_wall
		try:
			item = GoodCommentVotes.objects.get(item=self, user=user)
			if item.vote != GoodCommentVotes.DISLIKE:
				item.vote = GoodCommentVotes.DISLIKE
				item.save(update_fields=['vote'])
				self.like -= 1
				self.dislike += 1
				self.save(update_fields=['like', 'dislike'])
			else:
				item.delete()
				self.dislike -= 1
				self.save(update_fields=['dislike'])
		except GoodCommentVotes.DoesNotExist:
			GoodCommentVotes.objects.create(item=self, user=user, vote=GoodCommentVotes.DISLIKE)
			self.dislike += 1
			self.save(update_fields=['dislike'])
			if self.parent:
				if community:
					from common.notify.notify import community_notify, community_wall
					community_notify(user, community, None, self.pk, "POSC", "u_good_comment_notify", "DRE")
					community_wall(user, community, None, self.pk, "POSC", "u_good_comment_notify", "DCO")
				else:
					from common.notify.notify import user_notify, user_wall
					user_notify(user, None, self.pk, "GOOC", "u_good_comment_notify", "DRE")
					user_wall(user, None, self.pk, "GOOC", "u_good_comment_notify", "DCO")
			else:
				if community:
					from common.notify.notify import community_notify, community_wall
					community_notify(user, community, None, self.pk, "POSC", "u_good_comment_notify", "DCO")
					community_wall(user, community, None, self.pk, "POSC", "u_good_comment_notify", "DCO")
				else:
					from common.notify.notify import user_notify, user_wall
					user_notify(user, None, self.pk, "GOOC", "u_good_comment_notify", "DCO")
					user_wall(user, None, self.pk, "GOOC", "u_good_comment_notify", "DCO")
		return HttpResponse(json.dumps({"like_count": str(self.likes_count()),"dislike_count": str(self.dislikes_count())}),content_type="application/json")

	def delete_comment(self):
		from notify.models import Notify, Wall
		if self.status == "PUB":
			self.status = GoodComment.THIS_DELETED
		elif self.status == "EDI":
			self.status = GoodComment.THIS_EDITED_DELETED
		self.save(update_fields=['status'])
		if self.parent:
			self.parent.good.comment -= 1
			self.parent.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").update(status="C")
		else:
			self.good.comment -= 1
			self.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").update(status="C")
		if Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").exists():
			Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").update(status="C")
	def restore_comment(self):
		from notify.models import Notify, Wall
		if self.status == "_DEL":
			self.status = GoodComment.PUBLISHED
		elif self.status == "_DELE":
			self.status = GoodComment.EDITED
		self.save(update_fields=['status'])
		if self.parent:
			self.parent.good.comment += 1
			self.parent.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").update(status="R")
		else:
			self.good.comment += 1
			self.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").update(status="R")
		if Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").exists():
			Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").update(status="R")

	def close_item(self):
		from notify.models import Notify, Wall
		if self.status == "PUB":
			self.status = GoodComment.THIS_CLOSED
		elif self.status == "EDI":
			self.status = GoodComment.THIS_EDITED_CLOSED
		self.save(update_fields=['status'])
		if self.parent:
			self.parent.good.comment -= 1
			self.parent.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").update(status="C")
		else:
			self.good.comment -= 1
			self.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").update(status="C")
		if Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").exists():
			Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").update(status="C")
	def abort_close_item(self):
		from notify.models import Notify, Wall
		if self.status == "_CLO":
			self.status = GoodComment.PUBLISHED
		elif self.status == "_CLOE":
			self.status = GoodComment.EDITED
		self.save(update_fields=['status'])
		if self.parent:
			self.parent.good.comment += 1
			self.parent.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="REP").update(status="R")
		else:
			self.good.comment += 1
			self.good.save(update_fields=["comment"])
			if Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").exists():
				Notify.objects.filter(type="GOOC", object_id=self.pk, verb__contains="COM").update(status="R")
		if Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").exists():
			Wall.objects.filter(type="GOOC", object_id=self.pk, verb="COM").update(status="R")
