from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Advert
        fields = ['url',
                  'advert_title',
                  'slug',
                  'advert_category',
                  'rooms', 'price', 'area',
                  'year', 'building_type',
                  'description']
