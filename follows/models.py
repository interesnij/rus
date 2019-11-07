from django.db import models
from notifications.models import Notification, notification_handler, CommunityNotification, community_notification_handler
from django.conf import settings
from communities.models import Community


class Follow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, related_name='follows', verbose_name="Подписчик")
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, related_name='followers', null=False, verbose_name="На кого подписывается")

    def notification_follow(self, user):
        notification_handler(user, self.followed_user, Notification.CONNECTION_REQUEST, action_object=self, id_value=str(user.uuid), key='notification')

    class Meta:
        unique_together = ('user', 'followed_user')
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


    @classmethod
    def create_follow(cls, user_id, followed_user_id):
        follow = Follow.objects.create(user_id=user_id, followed_user_id=followed_user_id)
        return follow


class CommunityFollow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, related_name='follows', verbose_name="Подписчик")
    community = models.ForeignKey(Community, db_index=False, on_delete=models.CASCADE, related_name='community', null=False, verbose_name="На какое сообщество подписывается")

    def notification_follow(self, user):
        community_notification_handler(user, self.community, CommunityNotification.CONNECTION_REQUEST, action_object=self, id_value=str(user.uuid), key='notification')

    class Meta:
        unique_together = ('user', 'community')
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


    @classmethod
    def create_follow(cls, user_id, community_id):
        follow = CommunityFollow.objects.create(user_id=user_id, community_id=community_id)
        return follow
