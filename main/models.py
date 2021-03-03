from django.contrib.auth.models import Group, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from .constants import BUILDING_TYPE, PROFILE_TYPE

from functools import wraps


class Subscribe(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='subscribe_users')
    active = models.BooleanField(default=True)


class Profile(models.Model):
    """
        Модель клиента (пользователь сайта) который может
        быть в роли продавца/покупателя, арендатора/съемщика
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь')
    profile_type = models.CharField(
        max_length=20,
        choices=PROFILE_TYPE,
        null=True, blank=True
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        null=True, blank=True)

    class Meta:
        verbose_name = 'Профили'
        verbose_name_plural = 'Профиль'

    def __str__(self):
        return self.user.username


def disable_for_loaddata(signal_handler):
    """
    Decorator that turns off signal handlers when loading fixture data.
    """
    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        if kwargs['raw']:
            return
        signal_handler(*args, **kwargs)
    return wrapper


@receiver(post_save, sender=User)
@disable_for_loaddata
def create_customer_profile(
        sender: User,
        instance: User,
        created, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)
        instance.email = instance.email
        instance.groups.add(Group.objects.get(name='common_users'))


@receiver(post_save, sender=Profile)
@disable_for_loaddata
def add_user_to_realtor_group(sender: Profile,
                              instance: Profile, **kwargs) -> None:
    if instance.profile_type == 'realtor':
        instance.user.groups.add(Group.objects.get(name='realtor'))


class Category(models.Model):
    """ Модель категорий недвижимости """
    category_title = models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.category_title


class Advert(models.Model):
    """ Модель объявления """
    advert_title = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        null=True, blank=True)
    slug = models.SlugField(unique=True, verbose_name='ЧПУ')
    advert_owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Владелец объявления',
        null=True, blank=True)
    advert_category = ArrayField(
        models.CharField(max_length=100),
        verbose_name='Категории',
        blank=True, null=True)
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес дома',
        null=True, blank=True)
    rooms = models.IntegerField(verbose_name='Количество комнат')
    price = models.IntegerField(verbose_name='Цена')
    area = models.IntegerField(verbose_name='Общая площадь')
    year = models.IntegerField(verbose_name='Год постройки')
    building_type = models.CharField(
        max_length=30,
        choices=BUILDING_TYPE,
        default=None,
        verbose_name='Тип дома'
    )
    created = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-id']

    def __str__(self) -> str:
        return f"{self.advert_title}, {self.rooms}"

    def get_absolute_url(self) -> str:
        return reverse('advert-detail', kwargs={'pk': self.pk})

    @property
    def price_per_square_meter(self) -> float:
        return round(self.price / self.area, 2)


class Apartment(Advert):
    """ Модель квартиры """
    floors = models.PositiveIntegerField(
        default=1,
        verbose_name='Этажность дома')
    apartment_floor = models.PositiveIntegerField(
        default=1,
        verbose_name='Номер этажа')

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'

    def __str__(self) -> str:
        return self.advert_title


class House(Advert):
    """ Модель дома """
    garage = models.BooleanField(
        default=False,
        verbose_name='Гараж')
    plot = models.FloatField(
        default=0.00,
        verbose_name="Участок")

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self) -> str:
        return self.advert_title
