from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('tutorials.urls')),
]
from monitor.handlers import grpc_handlers as monitor_grpc_handlers


urlpatterns = [
    path("admin", admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]


def grpc_handlers(server):
    monitor_grpc_handlers(server)
    