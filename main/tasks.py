from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from main.models import Advert
from django.utils import timezone

from conf import settings
from main.celery import app
from main.models import Subscribe


@app.task()
def newsletter(subject, object_list=None, **kwargs):
    mail_list = Subscribe.objects.values_list('user__email', flat=True)
    from_email = settings.DEFAULT_FROM_EMAIL
    if object_list:
        context = {'subject': subject, 'object_list': object_list}
    else:
        title = kwargs.get('title')
        price = kwargs['price']
        context = {'subject': subject, 'title': title, 'price': price}
    html_content = render_to_string('news/news.html', context=context)

    for email in mail_list:
        msg = EmailMultiAlternatives(
            subject,
            html_content,
            from_email,
            [email])
        msg.content_subtype = 'html'
        msg.send()


@app.task()
def news():
    # Отправлять сводку еженедельных подборок товаров через celery
    tm = timezone.now() - timezone.timedelta(days=7)
    object_list = Advert.objects.filter(created__gte=tm).only(
        'advert_title', 'price')[:9]
    newsletter(subject='Новое за неделю', object_list=object_list)
