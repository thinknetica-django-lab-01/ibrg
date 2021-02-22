from django.urls import path

from .views import (AdvertDetailView, AdvertListView, AdvertUpdate,
                    ApartmentCreateView, HouseCreateView, Profile, index,
                    update_profile, subscribe,)

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    # Profile
    path('accounts/profile/', Profile.as_view(),
         name='profile'),
    path('accounts/profile/update/', update_profile,
         name='update_profile'),
    # main
    path('', index, name='index'),
    path('adverts/', AdvertListView.as_view(),
         name='adverts-list'),
    path('<slug:category_slug>/', AdvertListView.as_view(),
         name='adverts-list'),
    path('detail/<int:pk>/', AdvertDetailView.as_view(),
         name='advert-detail'),
    path('add/apartment/', ApartmentCreateView.as_view(),
         name='add_apartment'),
    path('add/house/', HouseCreateView.as_view(),
         name='add_house'),
    path('update/<slug:slug>/', AdvertUpdate.as_view(),
         name='update_advert'),
]
