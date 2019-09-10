from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifications.consumers import NoseyConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})
