from django.apps import AppConfig
from django.conf import settings
from .redis_pool import PortPool

class TopicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topic'

    def ready(self):
        import topic.signals
        port_pool=PortPool()
        port_pool.initialize_pool()