# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chaotix.settings")
app = Celery("chaotix")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()