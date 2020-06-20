from gallery.view.user_progs import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns=[
    url(r'^description/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserPhotoDescription.as_view()),
    url(r'^delete/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserPhotoDelete.as_view()),
    url(r'^abort_delete/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserPhotoAbortDelete.as_view()),
    url(r'^on_comment/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserOpenCommentPhoto.as_view()),
    url(r'^off_comment/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserCloseCommentPhoto.as_view()),
    url(r'^on_private/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserOnPrivatePhoto.as_view()),
    url(r'^off_private/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserOffPrivatePhoto.as_view()),
    url(r'^add_avatar/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserAddAvatarPhoto.as_view()),
    url(r'^remove_avatar/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserRemoveAvatarPhoto.as_view()),

    url(r'^comment/(?P<uuid>[0-9a-f-]+)/(?P<pk>\d+)/$', PhotoUserCommentList.as_view()),
    url(r'^post-comment/$', login_required(PhotoCommentUserCreate.as_view())),
    url(r'^reply-comment/$', login_required(PhotoReplyUserCreate.as_view())),
]
