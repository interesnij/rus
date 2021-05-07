from django.conf.urls import url
from video.view.user_progs import *


urlpatterns = [
    url(r'^create_video/(?P<pk>\d+)/$', UserVideoCreate.as_view()),
    url(r'^edit/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserVideoEdit.as_view()),
    url(r'^delete/(?P<uuid>[0-9a-f-]+)/$', UserVideoDelete.as_view()),
    url(r'^restore/(?P<uuid>[0-9a-f-]+)/$', UserVideoAbortDelete.as_view()),
    url(r'^on_comment/(?P<uuid>[0-9a-f-]+)/$', UserOpenCommentVideo.as_view()),
    url(r'^off_comment/(?P<uuid>[0-9a-f-]+)/$', UserCloseCommentVideo.as_view()),
    url(r'^on_private/(?P<uuid>[0-9a-f-]+)/$', UserOnPrivateVideo.as_view()),
    url(r'^off_private/(?P<uuid>[0-9a-f-]+)/$', UserOffPrivateVideo.as_view()),
    url(r'^on_votes/(?P<uuid>[0-9a-f-]+)/$', UserOnVotesVideo.as_view()),
    url(r'^off_votes/(?P<uuid>[0-9a-f-]+)/$', UserOffVotesVideo.as_view()),
    url(r'^add_video_in_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', AddVideoInUserList.as_view()),
    url(r'^remove_video_from_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', RemoveVideoFromUserList.as_view()),

    url(r'^post-comment/$', VideoCommentUserCreate.as_view()),
    url(r'^reply-comment/$', VideoReplyUserCreate.as_view()),
    url(r'^delete_comment/(?P<pk>\d+)/$', VideoCommentUserDelete.as_view()),
	url(r'^restore_comment/(?P<pk>\d+)/$', VideoCommentUserAbortDelete.as_view()),

    url(r'^create_list/(?P<pk>\d+)/$', UserVideoListCreate.as_view()),
    url(r'^edit_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserVideolistEdit.as_view()),
    url(r'^delete_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserVideolistDelete.as_view()),
    url(r'^restore_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserVideolistAbortDelete.as_view()),
    url(r'^add_list_in_collections/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', AddVideoListInUserCollections.as_view()),
    url(r'^remove_list_from_collections/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', RemoveVideoListFromUserCollections.as_view()),
]
