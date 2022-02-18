from django.conf.urls import url
from managers.view.article import *


urlpatterns = [
    url(r'^create_rejected/(?P<pk>\d+)/$', MailRejectedCreate.as_view()),
    url(r'^unverify/(?P<uuid>[0-9a-f-]+)/$', MailUnverify.as_view()),
]
