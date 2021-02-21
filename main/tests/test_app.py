import os
import django

import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse
from main.models import Advert
from django.contrib.auth.models import User, Group

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
django.setup()


@pytest.mark.django_db
class TestAdvertView:

    @pytest.fixture(scope="function")
    def set_obj(self):
        for x in range(1, 21):
            Advert.objects.create(
                advert_title=f'Advert title {x}',
                slug=f'advert-slug-{x}',
                rooms=2, price=20000, area=54, year=f'{2010 + 1}',
                building_type='brick')

    @pytest.fixture(scope="function")
    def test_user(self, client):
        """
        Создаем пользователя та группы чтобы получить
        доступ к добавлению обьявлений
        """
        username = "TT42"
        password = "424242"
        # Создаем группы
        Group.objects.create(name='common_users')
        Group.objects.create(name='realtor')
        # создаем список с групами
        user_group = Group.objects.filter(name__in=['realtor', 'common_users'])
        # Создаем пользователя
        User.objects.create(username=username, password=password)
        self.user = User.objects.get(id=1)
        # Добавляем пользователя в групы
        self.user.groups.add(*user_group)

    def test_advert_count(self, set_obj):
        assert Advert.objects.count() == 20

    def test_advert_house_create(self, test_user, client):
        # Авторизуем созданого пользователя
        client.force_login(self.user)

        url = reverse('add_house')
        data = {
            'advert_title': 'House 42',
            'slug': 'house-42',
            'rooms': 42,
            'price': 424242,
            'area': 42,
            'year': 2042,
            'building_type': 'brick'
        }
        obj = client.post(url, data)
        assert obj.status_code == 200

    # Тестирование ответа сервера
    def test_adverts_get_url(self, client):
        resp = client.get(reverse('adverts-list'))
        assert resp.status_code == 200

    def test_advert_detail(self, set_obj, client):
        url = reverse('advert-detail', args=[10, ])
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
