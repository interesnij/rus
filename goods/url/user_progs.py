from goods.view.user_progs import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns=[
    url(r'^on_comment/(?P<pk>\d+)/$', UserOpenCommentGood.as_view()),
    url(r'^off_comment/(?P<pk>\d+)/$', UserCloseCommentGood.as_view()),
    url(r'^hide/(?P<pk>\d+)/$', UserHideGood.as_view()),
    url(r'^unhide/(?P<pk>\d+)/$', UserUnHideGood.as_view()),
    url(r'^on_votes/(?P<pk>\d+)/$', UserOnVotesGood.as_view()),
    url(r'^off_votes/(?P<pk>\d+)/$', UserOffVotesGood.as_view()),

    url(r'^post-comment/$', login_required(GoodCommentUserCreate.as_view())),
    url(r'^reply-comment/$', login_required(GoodReplyUserCreate.as_view())),
    url(r'^delete_comment/(?P<pk>\d+)/$', login_required(GoodCommentUserDelete.as_view())),
	url(r'^restore_comment/(?P<pk>\d+)/$', login_required(GoodCommentUserAbortDelete.as_view())),

    url(r'^add/$', GoodUserCreate.as_view()),
    url(r'^edit/(?P<pk>\d+)/$', GoodUserEdit.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', UserGoodDelete.as_view()),
    url(r'^restore/(?P<pk>\d+)/$', UserGoodAbortDelete.as_view()),
    url(r'^add_good_in_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', AddGoodInUserList.as_view()),
    url(r'^remove_good_in_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', RemoveGoodInUserList.as_view()),

    url(r'^add_list/(?P<pk>\d+)/$', GoodListUserCreate.as_view()),
    url(r'^edit_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserGoodListEdit.as_view()),
    url(r'^delete_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserGoodListDelete.as_view()),
    url(r'^restore_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserGoodListAbortDelete.as_view()),
    url(r'^add_list_in_collections/(?P<uuid>[0-9a-f-]+)/$', AddGoodListInUserCollections.as_view()),
    url(r'^remove_list_from_collections/(?P<uuid>[0-9a-f-]+)/$', RemoveGoodListFromUserCollections.as_view()),
]
