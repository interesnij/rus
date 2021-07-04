from django.db.models import Q
from notify.models import Wall


def get_news(user):
    """ лента новостей, куда попадают все записи уведомлений с вхождениями:
        1. создатель пользователь, если это пост, фото, видео, товар, и т.д.
        2. создатели - все пользователи, id которых хранит таблица UserNotify, где user - пользователь (те, на которых подписан пользователь или с кем дружит)
        3. сообщетсва - все сообщества, id которых хранит таблица CommunityNotify, user - пользователь (те, на которых подписан пользователь)
        Примечания:
        - список покажет все уведомления по времени. Там будут только разрешенные публичные записи, приватное же просто не создаст уведомления.
            ведь никто их не увидит кроме пользователя и значит реагировать на них не сможет .
        - прикрепленные элементы просто записаны в текстовое поле, например pho_19 - это фотка под номером 19. Так
            пользователь увидит все действия, как и в контакте.
    """
    query = Q(Q(creator_id=user.pk)|Q(creator_id__in=user.get_user_news_notify_ids())|Q(community_id__in=user.get_community_news_notify_ids())) \
    &Q(verb="ITE")
    query.add(Q(object_set__isnull=True), Q.AND)
    query.add(~Q(status="C"), Q.AND)
    return Wall.objects.filter(query)

def get_featured_news(user):
    """ лента новостей, куда попадают все записи уведомлений с вхождениями:
        1. создатель пользователь, если это пост, фото, видео, товар, и т.д.
        2. создатели - все пользователи, id которых хранит таблица UserNotify, где user - пользователь (те, на которых подписан пользователь или с кем дружит)
        3. сообщетсва - все сообщества, id которых хранит таблица CommunityNotify, user - пользователь (те, на которых подписан пользователь)
        Примечания:
        - список покажет все уведомления по времени. Там будут только разрешенные публичные записи, приватное же просто не создаст уведомления.
            ведь никто их не увидит кроме пользователя и значит реагировать на них не сможет .
        - прикрепленные элементы просто записаны в текстовое поле, например pho_19 - это фотка под номером 19. Так
            пользователь увидит все действия, как и в контакте.
    """
    query = Q(creator_id__in=user.get_possible_friends_ids())|Q(community_id__in=user.get_6_possible_friends_communities_ids())
    query.add(Q(object_set__isnull=True), Q.AND)
    query.add(~Q(status="C"), Q.AND)
    return Wall.objects.filter(query)
