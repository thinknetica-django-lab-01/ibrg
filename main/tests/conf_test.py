import pytest
from main.models import Advert


@pytest.fixture(scope='session')
def setup_func(request):
    for x in range(7):
        Advert.objects.create(
            advert_title=f'Advert title {x}',
            slug=f'advert-slug-{x}',
            rooms=2, price=20000, area=54, year=f'{2010 + 1}',
            building_type='brick')
    return locals()