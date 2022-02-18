from django.conf.urls import url
from managers.view.photo import *


urlpatterns = [
    url(r'^delete_close/(?P<uuid>[0-9a-f-]+)/$', PhotoCloseDelete.as_view()),
    url(r'^create_rejected/(?P<pk>\d+)/$', PhotoRejectedCreate.as_view()),
    url(r'^unverify/(?P<uuid>[0-9a-f-]+)/$', PhotoUnverify.as_view()),

    url(r'^list_delete_close/(?P<uuid>[0-9a-f-]+)/$', ListPhotoCloseDelete.as_view()),
    url(r'^list_create_rejected/(?P<pk>\d+)/$', ListPhotoRejectedCreate.as_view()),
    url(r'^list_unverify/(?P<uuid>[0-9a-f-]+)/$', ListPhotoUnverify.as_view()),

    url(r'^comment_delete_close/(?P<pk>\d+)/$', CommentPhotoCloseDelete.as_view()),
    url(r'^comment_create_rejected/(?P<pk>\d+)/$', CommentPhotoRejectedCreate.as_view()),
    url(r'^comment_unverify/(?P<pk>\d+)/$', CommentPhotoUnverify.as_view()),
]
