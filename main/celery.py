import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



app.conf.beat_schedule = {
    'say_hello': {
        'task': 'main.tasks.print_hello',
        'schedule': 15.0
    }
}