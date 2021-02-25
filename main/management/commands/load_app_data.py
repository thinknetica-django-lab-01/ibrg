from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from main.models import Apartment, House


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for x in range(total):
            Apartment.objects.create(
                advert_title=f'Квартира {x}',
                slug=get_random_string(),
                rooms='3',
                price=20000 * int(x),
                area=20 + int(x),
                year='2042',
                floors='5',
                apartment_floor='4',
                building_type='brick',
            )
            House.objects.create(
                advert_title=f'House {x}',
                slug=get_random_string(),
                rooms=3,
                price=20000 * int(x),
                area=60,
                year='2003',
                building_type='brick',
                garage='1'
            )
        self.stdout.write(self.style.SUCCESS(
            f'Успешно добавлено {total} объектов'
        ))
