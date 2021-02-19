import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
django.setup()

import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from main.models import Advert, House


@pytest.mark.django_db
class TestAdvertView:

    @pytest.fixture(scope="function")
    def set_obj(self):
        for x in range(1,21):
            obj = Advert.objects.create(
                advert_title=f'Advert title {x}',
                slug=f'advert-slug-{x}',
                rooms=2, price=20000, area=54, year=f'{2010 + 1}',
                building_type='brick')

    def test_advert_count(self, set_obj):
        assert Advert.objects.count() == 20

    def test_advert_house_create(self):
        assert House.objects.count() == 0
        obj = House.objects.create(
            advert_title = 'House 42',
            slug = 'house-42',
            rooms = 42, price = 424242, 
            area = 42, year=2042,
            building_type = 'brick'
        )
        assert House.objects.count() == 1
        assert obj.advert_title == 'House 42'
        assert obj.price == 424242

     # Тестирование ответа сервера
    def test_adverts_get_url(self, client):
        resp = client.get(reverse('adverts-list'))
        assert resp.status_code == 200

    def test_advert_detail(self, set_obj, client):
        url = reverse('advert-detail', args = [10,])
        response = client.get(url)
        assert response.status_code == 200

    # Тестирование корректного получение шаблона
    def test_view_correct_template(self, client):
        resp = client.get(reverse('adverts-list'))
        assert resp.status_code == 200
        assertTemplateUsed(resp, 'main/advert_list.html')

    def test_detail_view_correct_template(self, set_obj, client):
        obj = Advert.objects.get(pk=10)
        resp = client.get(reverse('advert-detail', args=[obj.pk]))
        assert resp.status_code == 200
        assertTemplateUsed(resp, 'main/advert_detail.html')


