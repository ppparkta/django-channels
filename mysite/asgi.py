import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django_asgi_app = get_asgi_application()
# django_asgi_app 다음에 import chat.routing 코드 작성해야 인식 가능함
# loading 후에 실행 시켜야 함
# noqa는 린트 무시하는 주석 명령어 (꿀팁)
import chat.routing # noqa

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns),
    ),
})