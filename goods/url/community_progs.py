from goods.view.community_progs import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns=[
    url(r'^delete/(?P<pk>\d+)/$', CommunityGoodDelete.as_view()),
    url(r'^abort_delete/(?P<pk>\d+)/$', CommunityGoodAbortDelete.as_view()),
    url(r'^on_comment/(?P<pk>\d+)/$', CommunityOpenCommentGood.as_view()),
    url(r'^off_comment/(?P<pk>\d+)/$', CommunityCloseCommentGood.as_view()),
    url(r'^hide/(?P<pk>\d+)/$', CommunityHideGood.as_view()),
    url(r'^unhide/(?P<pk>\d+)/$', CommunityUnHideGood.as_view()),
    url(r'^on_votes/(?P<pk>\d+)/$', CommunityOnVotesGood.as_view()),
    url(r'^off_votes/(?P<pk>\d+)/$', CommunityOffVotesGood.as_view()),

    url(r'^post-comment/$', login_required(GoodCommentCommunityCreate.as_view())),
    url(r'^reply-comment/$', login_required(GoodReplyCommunityCreate.as_view())),
    url(r'^delete_comment/(?P<pk>\d+)/$', login_required(GoodCommentCommunityDelete.as_view())),
	url(r'^abort_delete_comment/(?P<pk>\d+)/$', login_required(GoodCommentCommunityAbortDelete.as_view())),

    url(r'^add/(?P<pk>\d+)/$', GoodCommunityCreate.as_view()),

    url(r'^add_list/(?P<pk>\d+)/$', GoodListCommunityCreate.as_view()),
    url(r'^edit_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityGoodListEdit.as_view()),
    url(r'^delete_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityGoodListDelete.as_view()),
    url(r'^abort_delete_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityGoodListAbortDelete.as_view()),
    url(r'^add_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityGoodListAdd.as_view()),
    url(r'^remove_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', CommunityGoodListRemove.as_view()),
]
