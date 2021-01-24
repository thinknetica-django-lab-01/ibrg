from django.db import models
from django.contrib.auth import get_user_model
from .constants import ADVERT_TYPE, PROFILE_TYPE, BUILDING_TYPE

User = get_user_model()


class Customer(models.Model):
    '''
        Модель клиента (пользователь сайта) который может
        быть в роли продавца/покупателя, арендатора/съемщика
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь')
    profile_type = models.CharField(
        max_length=20,
        choices=PROFILE_TYPE,
        default=None,
    )
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.user.username


class Category(models.Model):
    ''' Модель категорий недвижимости '''
    category_title = models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_title


class Advert(models.Model):
    ''' Модель объявления '''

    class Meta:
        abstract = True

    advert_title = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        null=True, blank=True)
    advert_slug = models.SlugField(unique=True, verbose_name='ЧПУ')
    advert_owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Владелец объявления',
        null=True, blank=True)
    advert_category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name='Категория',
        null=True, blank=True)
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес дома',
        null=True, blank=True)
    rooms = models.IntegerField(verbose_name='Количество комнат')
    price = models.IntegerField(verbose_name='Цена')
    area = models.IntegerField(verbose_name='Общая площадь')
    year = models.IntegerField(verbose_name='Год постройки')
    building_type =  models.CharField(
        max_length=30,
        choices=BUILDING_TYPE,
        default=None,
        verbose_name='Тип дома'
    )

    def __str__(self):
        return self.advert_title


class Apartment(Advert):
    ''' Модель квартиры '''
    floors = models.IntegerField(default=1, verbose_name='Этажность дома')
    apartment_floor = models.IntegerField(default=1, verbose_name='Номер этажа')

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'

    def __str__(self):
        return f'{self.advert_category}, {self.advert_title}'


class House(Advert):
    ''' Модель дома '''
    garage = models.BooleanField(default=False, verbose_name='Гараж')
    plot = models.FloatField(default=0.00, verbose_name="Участок")

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return f'{self.advert_category}, {self.advert_title}'
