from django.conf.urls import url
from docs.view.user_progs import *


urlpatterns = [
    url(r'^create_list/$', UserDocListCreate.as_view()),
    url(r'^edit_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserDocListEdit.as_view()),
    url(r'^delete_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserDocListDelete.as_view()),
    url(r'^restore_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserDocListAbortDelete.as_view()),
    url(r'^add_list_in_collections/(?P<uuid>[0-9a-f-]+)/$', AddDocListInUserCollections.as_view()),
    url(r'^remove_list_from_collections/(?P<uuid>[0-9a-f-]+)/$', RemoveDocListFromUserCollections.as_view()),

    url(r'^create_doc/(?P<pk>\d+)/$', UserDocCreate.as_view()),
    url(r'^edit_doc/(?P<doc_pk>\d+)/$', UserDocEdit.as_view()),
    url(r'^remove_doc/(?P<doc_pk>\d+)/$', UserDocRemove.as_view()),
    url(r'^restore_doc/(?P<doc_pk>\d+)/$', UserDocAbortRemove.as_view()),
    url(r'^add_doc_in_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserDocListAdd.as_view()),
    url(r'^remove_doc_in_list/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserDocListRemove.as_view()),
]
