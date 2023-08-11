from django.urls import path
from . import consumers

# urls.py의 websocket 버전
websocket_urlpatterns = [
    path("ws/chat/<int:room_pk>/", consumers.RolePlayingRoomConsumer.as_asgi()),
]