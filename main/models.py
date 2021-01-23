from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    """
        Модель клиента (пользователь сайта) который может
        быть в роли продавца/покупателя, арендатора/съемщика
    """
    PROFILE_TYPE = [
        ('realtor', 'риелтор'),
        ('company', 'агентство'),
        ('developer', 'застройщик'),
        ('owner', 'собственник'),
    ]
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    profile_type = models.CharField(
        max_length=20,
        choices=PROFILE_TYPE,
        default=None,
    )
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)


class Category(models.Model):
    """ Модель категорий недвижимости """
    category_title = models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_title


class Advert(models.Model):
    """ Модель объявления """

    class Meta:
        abstract = True

    advert_title = models.CharField(max_length=100, null=True, )
    advert_slug = models.SlugField(unique=True)
    advert_owner = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Владелец объявления")
    advert_category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Адрес дома")
    rooms = models.IntegerField(verbose_name='Количество комнат')
    price = models.IntegerField(verbose_name='Цена')
    area = models.IntegerField(verbose_name="Общая площадь")
    year = models.IntegerField(verbose_name='Год постройки')

    def __str__(self):
        return self.advert_title


class Apartment(Advert):
    """ Модель квартиры """
    build_level = models.IntegerField(default=1, verbose_name='Количество этажей дома')
    apartment_floor = models.IntegerField(default=1, verbose_name='Номер этажа')

    def __str__(self):
        return f"{self.advert_category}, {self.advert_title}"


class House(Advert):
    """ Модель квартиры """
    HOUSE_TYPE = [
        ('house', 'дом'),
        ('cottage', 'коттедж')
    ]
    house_type = models.CharField(
        max_length=10,
        choices=HOUSE_TYPE,
        default=None,
    )
    garage = models.IntegerField(default=0, verbose_name='Гараж')


    def __str__(self):
        return f"{self.advert_category}, {self.advert_title}"


