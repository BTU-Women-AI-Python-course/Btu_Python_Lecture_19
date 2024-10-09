import os
from celery import Celery

# Set default Django settings for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Create Celery app
app = Celery('core')

# Load configuration from settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks automatically from your apps
app.autodiscover_tasks()
