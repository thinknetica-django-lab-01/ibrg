from django.test import TestCase
from django.urls import reverse

from main.models import Advert


class AdvertListTest(TestCase):
    """
    Тестирование ответа сервера, шаблон, пагинация
    """

    def setUp(self):
        for x in range(7):
            Advert.objects.create(
                advert_title=f'Advert title {x}',
                slug=f'advert-slug-{x}',
                rooms=2, price=20000, area=54, year=f'{2010 + 1}',
                building_type='brick')
        return locals()

    def test_create_advert(self):
        ad = Advert.objects.get(pk=1)
        self.assertEqual(ad.advert_title, 'Advert title 0')

    def test_views_url_exist(self):
        resp = self.client.get(reverse('adverts-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_correct_template(self):
        resp = self.client.get(reverse('adverts-list'))
        self.assertTemplateUsed(resp, 'main/advert_list.html')

    # test Detail object
    def test_get_absolute_url(self):
        advert = Advert.objects.get(id=1)
        self.assertEquals(advert.get_absolute_url(), '/detail/1/')

    def test_detail_view_correct_template(self):
        resp = self.client.get(reverse('advert-detail', args=[1]))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/advert_detail.html')
