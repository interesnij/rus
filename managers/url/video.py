from django.conf.urls import url
from managers.view.video import *


urlpatterns = [
    url(r'^delete_close/(?P<uuid>[0-9a-f-]+)/$', VideoCloseDelete.as_view()),
    url(r'^create_rejected/(?P<pk>\d+)/$', VideoRejectedCreate.as_view()),
    url(r'^unverify/(?P<video_uuid>[0-9a-f-]+)/$', VideoUnverify.as_view()),

    url(r'^list_delete_close/(?P<uuid>[0-9a-f-]+)/$', ListVideoCloseDelete.as_view()),
    url(r'^list_create_rejected/(?P<pk>\d+)/$', ListVideoRejectedCreate.as_view()),
    url(r'^list_unverify/(?P<uuid>[0-9a-f-]+)/$', ListVideoUnverify.as_view()),

    url(r'^comment_delete_close/(?P<pk>\d+)/$', CommentVideoCloseDelete.as_view()),
    url(r'^comment_create_rejected/(?P<pk>\d+)/$', CommentVideoRejectedCreate.as_view()),
    url(r'^comment_unverify/(?P<pk>\d+)/$', CommentVideoUnverify.as_view()),
]
