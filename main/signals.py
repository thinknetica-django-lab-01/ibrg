from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Apartment, House

from .tasks import newsletter


@receiver(post_save, sender=House)
@receiver(post_save, sender=Apartment)
def send_email_after_save_new_ad(sender, instance, created, **kwargs):
    # Реализовать рассылку уведомлений подписчикам на новинки товаров через celery задачи
    if created:
        subject = f'На сайте добавлено новый объект {instance.advert_title}'
        newsletter.delay(subject=subject, title=instance.advert_title, price=instance.price)
