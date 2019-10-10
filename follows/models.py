from django.db import models
from users.models import User
from notifications.models.notification import Notification, notification_handler



class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows', verbose_name="Подписчик")
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', null=False, verbose_name="На кого подписывается")

    def notification_follow(self, user):
        notification_handler(user, self.followed_user, Notification.CONNECTION_REQUEST, action_object=self, id_value=str(user.uuid), key='notification')
