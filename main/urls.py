from django.urls import path

from .views import AdvertListView, AdvertDetailView, CustomerProfileUpdate


urlpatterns = [
    path('', AdvertListView.as_view(), name='adverts-list'),
    path('<slug:category_slug>/', AdvertListView.as_view(), name='adverts-list'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
    path('accounts/profile/<int:pk>/', CustomerProfileUpdate.as_view(), name='update_profile'),


]
