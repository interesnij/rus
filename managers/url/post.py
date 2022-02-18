from django.conf.urls import url
from managers.view.post import *


urlpatterns = [
    url(r'^delete_close/(?P<uuid>[0-9a-f-]+)/$', PostCloseDelete.as_view()),
    url(r'^create_rejected/(?P<pk>\d+)/$', PostRejectedCreate.as_view()),
    url(r'^unverify/(?P<uuid>[0-9a-f-]+)/$', PostUnverify.as_view()),

    url(r'^list_delete_close/(?P<uuid>[0-9a-f-]+)/$', ListPostCloseDelete.as_view()),
    url(r'^list_create_rejected/(?P<pk>\d+)/$', ListPostRejectedCreate.as_view()),
    url(r'^list_unverify/(?P<uuid>[0-9a-f-]+)/$', ListPostUnverify.as_view()),

    url(r'^comment_delete_close/(?P<pk>\d+)/$', CommentPostCloseDelete.as_view()),
    url(r'^comment_create_rejected/(?P<pk>\d+)/$', CommentPostRejectedCreate.as_view()),
    url(r'^comment_unverify/(?P<pk>\d+)/$', CommentPostUnverify.as_view()),
]
