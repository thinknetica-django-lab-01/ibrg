from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        for x in range(total):
            User.objects.create_user(
                username=get_random_string(),
                password='123456'
            )
        self.stdout.write(self.style.SUCCESS(f'Добавлено {total} пользователей'))
