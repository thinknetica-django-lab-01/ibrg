from main.models import User, Category, Apartment, House

# Create user
user = User.objects.get_or_create(username='Ben', password='123456')
user = User.objects.get(username='Ben')


# add few category
c1 = Category.objects.create(
    category_title='Квартира в новостройке',
    category_slug='new_building')  # example 1
c1.save()

c2 = Category(2, 'Квартира во вторичке', 'resale')  # example 2
c2.save()

c3 = Category(3, 'Дом', 'house')
c3.save()

# add apartment
a1 = Apartment(
    advert_title = 'Первая квартира',
    advert_slug = 'first_flat',
    advert_owner = user,
    advert_category = c1,
    rooms = '1',
    price = '22000',
    area = '30',
    year = '2011',
    floors = '9',
    apartment_floor = '1'
)
a1.save()

a2 = Apartment(
    advert_title = 'Вторая квартира',
    advert_slug = 'second_flat',
    advert_owner = user,
    advert_category = c2,
    rooms = '2',
    price = '44000',
    area = '40',
    year = '1990',
    floors = '9',
    apartment_floor = '3'
)
a2.save()

a3 = Apartment(
    advert_title = 'Третья квартира',
    advert_slug = 'third_flat',
    advert_owner = user,
    advert_category = c1,
    rooms = '3',
    price = '66000',
    area = '50',
    year = '1965',
    floors = '5',
    apartment_floor = '4'
)
a3.save()

# add house
h1 = House(
    advert_title='Первый дом',
    advert_slug='first_house',
    advert_owner=user,
    advert_category=c3,
    rooms='3',
    price='66000',
    area='100',
    year='2011',
    house_type = 'house',
    garage = '1'
)
h1.save()
h2 = House(
    advert_title='Первый коттедж',
    advert_slug='first_cottage',
    advert_owner=user,
    advert_category=c3,
    rooms='4',
    price='100000',
    area='150',
    year='2015',
    house_type = 'cottage',
    garage = '1'
)
h2.save()

# get Appartment list
flats_list = Apartment.objects.all()

# filtering by category
flats_list.filter(advert_category=c2)