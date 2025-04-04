import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awd_django.settings')

app=Celery('django_celery')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()