from django.core.mail import send_mass_mail, EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from conf.settings import DEFAULT_FROM_EMAIL
from main.models import Subscribe, Advert, Apartment, House
from django.utils import timezone
from django.template.loader import render_to_string

@receiver(post_save, sender=House)
@receiver(post_save, sender=Apartment)
def send_email_after_save_new_ad(sender, instance, created, **kwargs):
    mail_list = Subscribe.objects.values_list('user__email', flat=True)
    from_email = DEFAULT_FROM_EMAIL
    subject = f'На сайте добавлено новый объект {instance.advert_title}'
    message = f'{instance.advert_title} <em>{instance.price} грн'
    message_tuple = []
    for email in mail_list:
        msg = (subject, message, from_email, [email])
        message_tuple.append(msg)
    print(*message_tuple)  # TODO: remove late
    send_mass_mail(message_tuple)




def news():
    "Оптарвка новый обьявлений подписчикам раз в неделю"
    tm = timezone.now() - timezone.timedelta(days=7)

    advert_list = Advert.objects.filter(created__gte=tm).only('advert_title', 'price')[:9]
    mail_list = Subscribe.objects.values_list('user__email', flat=True)

    from_email = DEFAULT_FROM_EMAIL
    context = {'advert_list': advert_list}
    html_content = render_to_string('news/news.html', context=context)
    subject = f'На сайте добавлено новый объект'

    for email in mail_list:
        msg = EmailMultiAlternatives(subject, html_content, from_email, [email])
        msg.content_subtype = 'html'
        msg.send()

    print('All send')
