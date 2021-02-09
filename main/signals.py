from django.core.mail import send_mass_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from conf.settings import DEFAULT_FROM_EMAIL
from main.models import Subscribe, Apartment, House


@receiver(post_save, sender=House)
@receiver(post_save, sender=Apartment)
def send_email_after_save_new_ad(sender, instance, created, **kwargs):
    mail_list = [subscribe.user.email for subscribe in Subscribe.objects.select_related('user')]
    from_email = DEFAULT_FROM_EMAIL
    subject = f'На сайте добавлено новый объект {instance.advert_title}'
    message = f'{instance.advert_title} <em>{instance.price} грн'
    message_tuple = []
    for email in mail_list:
        msg = (subject, message, from_email, [email])
        message_tuple.append(msg)
    print(*message_tuple)  # TODO: remove late
    send_mass_mail(message_tuple)


