from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from conf import settings
from main.signals import news


def start_job():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(news,
                      'cron',
                      # day_of_week='thu',
                      hour=1,
                      minute=48,
                      id='news',
                      max_instances=1,
                      replace_existing=True,
                      )

    scheduler.start()

    print('+' * 20)
    print('Start dsfsdgjsdfglkhsdf;lgkh∂')
    print('+' * 20)