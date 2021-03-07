from django.urls import path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from .views import (AdvertDetailView, AdvertListView, AdvertUpdate,
                    ApartmentCreateView, HouseCreateView, Profile, index,
                    update_profile, subscribe,)
from .models import Advert

info_dict = {
    'queryset': Advert.objects.all(),
    'date_field': 'created',
}

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
    path('<str:tag>/', AdvertListView.as_view(),
         name='adverts-list'),
    path('detail/<int:pk>/', AdvertDetailView.as_view(),
         name='advert-detail'),
    path('add/apartment/', ApartmentCreateView.as_view(),
         name='add_apartment'),
    path('add/house/', HouseCreateView.as_view(),
         name='add_house'),
    path('update/<slug:slug>/', AdvertUpdate.as_view(),
         name='update_advert'),
    # sitemap
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
