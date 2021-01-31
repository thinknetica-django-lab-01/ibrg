from django.urls import path

from .views import AdvertListView, AdvertDetailView, CustomerProfileUpdate, ApartmentCreateView, HouseCreateView, AdvertUpdate


urlpatterns = [
    path('', AdvertListView.as_view(), name='adverts-list'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
    path('add/apartment/', ApartmentCreateView.as_view(), name='add_apartment'),
    path('add/house/', HouseCreateView.as_view(), name='add_house'),
    path('update/<slug:slug>/', AdvertUpdate.as_view(), name='update_advert'),
    path('<slug:category_slug>/', AdvertListView.as_view(), name='adverts-list'),
    
    path('accounts/profile/<int:pk>/', CustomerProfileUpdate.as_view(), name='update_profile'),
]
