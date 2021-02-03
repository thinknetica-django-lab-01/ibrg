from django.urls import path

from .views import (
    AdvertListView,
    AdvertDetailView,
    CustomerProfileUpdate,
    ApartmentCreateView,
    HouseCreateView,
    AdvertUpdate,
    CustomerProfile,
    Login,
    index)

urlpatterns = [

    # Registration
    path('login/', Login.as_view(), name='login'),
    # Profile
    path('accounts/profile/<int:pk>/', CustomerProfile.as_view(), name='profile'),
    path('accounts/profile/<int:pk>/update/', CustomerProfileUpdate.as_view(), name='update_profile'),

    path('', index, name='index'),
    path('adverts/', AdvertListView.as_view(), name='adverts-list'),
    path('detail/<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
    path('add/apartment/', ApartmentCreateView.as_view(), name='add_apartment'),
    path('add/house/', HouseCreateView.as_view(), name='add_house'),
    path('update/<slug:slug>/', AdvertUpdate.as_view(), name='update_advert'),
    path('<slug:category_slug>/', AdvertListView.as_view(), name='adverts-list'),

]
