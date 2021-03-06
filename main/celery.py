import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('main')
app.config_from_object('django.conf:settings')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_news': {
        'task': 'main.tasks.news',
        'schedule': crontab(hour=19, minute=12, day_of_week='sun'),
    }
}
