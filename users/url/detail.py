from django.conf.urls import url
from users.views.detail import *
from users.views.lists import *

urlpatterns = [
    url(r'^item/(?P<pk>\d+)/(?P<uuid>[0-9a-f-]+)/$', UserItemView.as_view(), name='user_item'),
    url(r'^communities/(?P<uuid>[0-9a-f-]+)/$', UserCommunitiesList.as_view()),
    url(r'^manage_communities/(?P<uuid>[0-9a-f-]+)/$', UserManageCommunitiesList.as_view()),
    url(r'^list/(?P<pk>\d+)/$', ItemListView.as_view()),
    url(r'^possible/(?P<uuid>[0-9a-f-]+)/$', AllPossibleUsersList.as_view(), name='possible_users'),
    url(r'^music_list/(?P<uuid>[0-9a-f-]+)/$', UserMusicList.as_view()),
]
