from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore
from conf import settings
from main.signals import news


def start_job():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(news,
                      'cron',
                      day_of_week='fri',
                      hour=6,
                      minute=30,
                      id='news',
                      max_instances=1,
                      replace_existing=True,
                      )

    scheduler.start()

