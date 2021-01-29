from django.urls import path

from .views import AdvertListView, AdvertDetailView


urlpatterns = [
    path('', AdvertListView.as_view(), name='adverts-list'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),
]
