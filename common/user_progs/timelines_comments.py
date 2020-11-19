from django.db.models import Q
from posts.models import Post, PostComment
from gallery.models import Photo, PhotoComment
from goods.models import Good, GoodComment
from video.models import Video, VideoComment


def get_timeline_post_comments(user):
    """ лента записей, которые комментировал пользователь """
    posts = PostComment.objects.filter(commenter_id=user.pk, is_deleted=False).values("post_id")
    posts_ids = [post['post_id'] for post in posts]
    own_posts_query = Q(id__in=posts_ids, is_deleted=False, status=Post.STATUS_PUBLISHED)
    own_posts_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.post_creator.only('pk').filter(own_posts_query)

def get_timeline_photo_comments(user):
    """ лента фотографий, которые комментировал пользователь """
    photos = PhotoComment.objects.filter(commenter_id=user.pk, is_deleted=False).values("photo_comment_id")
    photos_ids = [photo['photo_comment_id'] for photo in photos]
    own_photos_query = Q(id__in=photos_ids, is_deleted=False, is_public=True)
    own_photos_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.photo_creator.only('pk').filter(own_photos_query)

def get_timeline_good_comments(user):
    """ лента товаров, которые комментировал пользователь """
    goods = GoodComment.objects.filter(commenter_id=user.pk, is_deleted=False).values("good_comment_id")
    goods_ids = [good['good_comment_id'] for good in goods]
    own_goods_query = Q(id__in=goods_ids, is_deleted=False, status=Good.STATUS_PUBLISHED)
    own_goods_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.good_creator.only('pk').filter(own_goods_query)

def get_timeline_video_comments(user):
    """ лента видеозаписей, которые комментировал пользователь """
    videos = VideoComment.objects.filter(commenter_id=user.pk, is_deleted=False).values("video_comment_id")
    videos_ids = [video['video_comment_id'] for video in videos]
    own_videos_query = Q(id__in=videos_ids, is_deleted=False, is_public=True)
    own_videos_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.video_creator.only('pk').filter(own_videos_query)


def get_timeline_featured_post_comments(user):
    """ лента записей, которые комментировали друзья пользователя и те, на кого он подписан """
    possible_users = user.get_friends_and_followings_ids()
    posts = PostComment.objects.filter(commenter_id__in=possible_users, is_deleted=False).values("post_id")
    posts_ids = [post['post_id'] for post in posts]
    own_posts_query = Q(id__in=posts_ids, is_deleted=False, status=Post.STATUS_PUBLISHED)
    own_posts_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.post_creator.only('pk').filter(own_posts_query)

def get_timeline_featured_photo_comments(user):
    """ лента фотографий, которые комментировали друзья пользователя и те, на кого он подписан """
    possible_users = user.get_friends_and_followings_ids()
    photos = PhotoComment.objects.filter(commenter_id__in=possible_users, is_deleted=False).values("photo_comment_id")
    photos_ids = [photo['photo_comment_id'] for photo in photos]
    own_photos_query = Q(id__in=photos_ids, is_deleted=False, is_public=True)
    own_photos_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.photo_creator.only('pk').filter(own_photos_query)

def get_timeline_featured_good_comments(user):
    """ лента товаров, которые комментировали друзья пользователя и те, на кого он подписан """
    possible_users = user.get_friends_and_followings_ids()
    goods = GoodComment.objects.filter(commenter_id__in=possible_users, is_deleted=False).values("good_comment_id")
    goods_ids = [good['good_comment_id'] for good in goods]
    own_goods_query = Q(id__in=goods_ids, is_deleted=False, status=Good.STATUS_PUBLISHED)
    own_goods_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.good_creator.only('pk').filter(own_goods_query)

def get_timeline_featured_video_comments(user):
    """ лента видеозаписей, которые комментировали друзья пользователя и те, на кого он подписан """
    possible_users = user.get_friends_and_followings_ids()
    videos = VideoComment.objects.filter(commenter_id__in=possible_users, is_deleted=False).values("video_comment_id")
    videos_ids = [video['video_comment_id'] for video in videos]
    own_videos_query = Q(id__in=videos_ids, is_deleted=False, is_public=True)
    own_videos_query.add(~Q(Q(creator__blocked_by_users__blocker_id=user.pk) | Q(creator__user_blocks__blocked_user_id=user.pk)), Q.AND)
    return user.video_creator.only('pk').filter(own_videos_query)
