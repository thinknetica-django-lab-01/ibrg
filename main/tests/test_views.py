from django.test import TestCase
from django.urls import reverse

from main.models import Advert



class AdvertListTest(TestCase):


    def setUp(self):
        for x in range(16):
            Advert.objects.create(
                advert_title=f'Advert title {x}', slug=f'advert-slug-{x}', rooms=2, price=20000, area=54, year=f'{2010+1}',
            building_type='brick')
        self.adverts = Advert.objects.all()

    def test_views_url_exist(self):
        resp = self.client.get('/adverts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_correct_template(self):
        resp = self.client.get('/adverts/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/advert_list.html')
    #
    def test_pagination_is_six(self):
        resp = self.client.get(reverse('adverts-list'), {'page': 2})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertEqual(len(resp.context['page_obj']), 6)



class AdvertDetailTest(TestCase):

    def setUp(self):
        for x in range(16):
            Advert.objects.create(
                advert_title=f'Advert title {x}', slug=f'advert-slug-{x}', rooms=2, price=20000, area=54, year=f'{2010+1}',
            building_type='brick')

    def test_get_absolute_url(self):
        advert = Advert.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(advert.get_absolute_url(), '/detail/1/')

        
    def test_detail_view_correct_tempate(self):
        resp = self.client.get(reverse('advert-detail', args=[10]))
        print(resp.context['advert'])
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/advert_detail.html')