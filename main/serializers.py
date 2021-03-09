from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        fields = ['id',
                  'advert_title',
                  'slug',
                  'advert_category',
                  'rooms', 'price', 'area',
                  'year', 'building_type',
                  'description']
