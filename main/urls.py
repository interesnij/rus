from django.conf.urls import url
from main.views import (
						MainPageView,
						ComingView,
						CommentLikeView,
						CommentDislikeView,
						DislikeView,
						LikeView,
						CommentLikeView,
						CommentDislikeView,
						get_comment,
						post_comment,
						reply_comment)
from django.contrib.auth.decorators import login_required


urlpatterns = [
	url(r'^$', ComingView.as_view(), name="coming"),
	url(r'^main/$', MainPageView.as_view(), name="main"),
	url(r'^main/like_window/(?P<pk>\d+)/$', LikeView.as_view(), name='like_window'),
	url(r'^main/dislike_window/(?P<pk>\d+)/$', DislikeView.as_view(), name='dislike_window'),
	url(r'^main/comment/$', get_comment, name='get_comment'),
    url(r'^main/post-comment/$', post_comment, name='post_comment'),
    url(r'^main/reply-comment/$', reply_comment, name='reply_comment'),
	url(r'^main/comment_like_window/(?P<pk>\d+)/$', CommentLikeView.as_view(), name='comment_like_window'),
	url(r'^main/comment_dislike_window/(?P<pk>\d+)/$', CommentDislikeView.as_view(), name='comment_dislike_window'),
]
