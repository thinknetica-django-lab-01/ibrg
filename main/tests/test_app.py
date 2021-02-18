import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
django.setup()

import pytest
from pytest_django.asserts import assertTemplateUsed
from .conf_test import setup_func
from django.urls import reverse
from main.models import Advert


@pytest.mark.django_db
class TestAdvertView:

    def set_obj(self):
        for x in range(1,20):
            Advert.objects.create(
                advert_title=f'Advert title {x}',
                slug=f'advert-slug-{x}',
                rooms=2, price=20000, area=54, year=f'{2010 + 1}',
                building_type='brick')

        ad = Advert.objects.get(pk=1)
        object_list = Advert.objects.all()
        return locals()

    def test_advert_create(self):
        obj = self.set_obj()['ad']
        assert obj.advert_title == 'Advert title 1'

    def test_adverts_get_url(self, client):
        resp = client.get(reverse('adverts-list'))
        assert resp.status_code == 200

    def test_view_correct_template(self, client):
        resp = client.get(reverse('adverts-list'))
        assert resp.status_code == 200
        assertTemplateUsed(resp, 'main/advert_list.html')

    def test_advert_detail(self, client):
        obj = self.set_obj()['ad']
        url = reverse(
            'advert-detail', kwargs={'pk': obj.pk}
        )
        response = client.get(url)
        assert response.status_code == 200

    def test_detail_view_correct_template(self, client):
        obj = self.set_obj()['ad']
        resp = client.get(reverse('advert-detail', kwargs={'pk': obj.pk}))
        assert resp.status_code == 200
        assertTemplateUsed(resp, 'main/advert_detail.html')


