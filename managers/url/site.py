from django.conf.urls import url
from managers.view.good import *


urlpatterns = [
    url(r'^create_rejected/(?P<pk>\d+)/$', SiteRejectedCreate.as_view()),
    url(r'^unverify/(?P<uuid>[0-9a-f-]+)/$', SiteUnverify.as_view()),
]
