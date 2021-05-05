from django.conf.urls import url
from posts.view.community_progs import *


urlpatterns = [
	url(r'^add_post/(?P<pk>\d+)/$', PostCommunityCreate.as_view()),
	url(r'^add_offer_post/(?P<pk>\d+)/$', PostOfferCommunityCreate.as_view()),

	url(r'^post-comment/$', login_required(PostCommunityCommentCreate.as_view())),
    url(r'^reply-comment/$', login_required(PostCommunityReplyCreate.as_view())),
	url(r'^delete_comment/(?P<pk>\d+)/(?P<comment_pk>\d+)/$', PostCommentCommunityDelete.as_view()),
	url(r'^abort_delete_comment/(?P<pk>\d+)/(?P<comment_pk>\d+)/$', PostCommentCommunityAbortDelete.as_view()),
	url(r'^delete_wall_comment/(?P<pk>\d+)/(?P<comment_pk>\d+)/$', PostWallCommentCommunityDelete.as_view()),
	url(r'^abort_delete_wall_comment/(?P<pk>\d+)/(?P<comment_pk>\d+)/$', PostWallCommentCommunityAbortDelete.as_view()),

	url(r'^fixed/(?P<uuid>[0-9a-f-]+)/$', PostCommunityFixed.as_view()),
    url(r'^unfixed/(?P<uuid>[0-9a-f-]+)/$', PostCommunityUnFixed.as_view()),
	url(r'^off_comment/(?P<uuid>[0-9a-f-]+)/$', PostCommunityOffComment.as_view()),
    url(r'^on_comment/(?P<uuid>[0-9a-f-]+)/$', PostCommunityOnComment.as_view()),
    url(r'^delete/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', PostCommunityDelete.as_view()),
	url(r'^wall_delete/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', PostWallCommunityDelete.as_view()),
	url(r'^abort_delete/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', PostCommunityAbortDelete.as_view()),
	url(r'^wall_abort_delete/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', PostWallCommunityAbortDelete.as_view()),
	url(r'^on_votes/(?P<uuid>[0-9a-f-]+)/$', CommunityOnVotesPost.as_view()),
    url(r'^off_votes/(?P<uuid>[0-9a-f-]+)/$', CommunityOffVotesPost.as_view()),

	url(r'^add_list/(?P<pk>\d+)/$', CommunityPostListCreate.as_view()),
    url(r'^edit_list/(?P<pk>\d+)/(?P<list_pk>\d+)/$', CommunityPostListEdit.as_view()),
    url(r'^delete_list/(?P<pk>\d+)/(?P<list_pk>\d+)/$', CommunityPostListDelete.as_view()),
    url(r'^abort_delete_list/(?P<pk>\d+)/(?P<list_pk>\d+)/$', CommunityPostListAbortDelete.as_view()),
	url(r'^add_list_in_collections/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', AddPostListInCommunityCollections.as_view()),
    url(r'^remove_list_from_collections/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', RemovePostListFromCommunityCollections.as_view()),
]
