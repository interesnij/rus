from django.urls  path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/$', consumers.ChatConsumer),
]
