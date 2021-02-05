from django.urls import path

from .views import (
    AdvertListView,
    AdvertDetailView,
    update_profile,
    ApartmentCreateView,
    HouseCreateView,
    AdvertUpdate,
    CustomerProfile,
<<<<<<< HEAD
    Login,
=======
>>>>>>> 5_2_django_allauth
    index)

urlpatterns = [

    # Profile
    path('accounts/profile/<int:pk>/', CustomerProfile.as_view(), name='profile'),
    path('accounts/profile/update/', update_profile, name='update_profile'),

<<<<<<< HEAD
=======
    # main
>>>>>>> 5_2_django_allauth
    path('', index, name='index'),
    path('adverts/', AdvertListView.as_view(), name='adverts-list'),
    path('detail/<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
    path('add/apartment/', ApartmentCreateView.as_view(), name='add_apartment'),
    path('add/house/', HouseCreateView.as_view(), name='add_house'),
    path('update/<slug:slug>/', AdvertUpdate.as_view(), name='update_advert'),
    path('<slug:category_slug>/', AdvertListView.as_view(), name='adverts-list'),

]
