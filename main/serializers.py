from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.ModelSerializer):

    # Корректно работает через Postman
    advert_category = serializers.ListField(
        child=serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False))

    class Meta:
        model = Advert
        fields = ['advert_title',
                  'slug',
                  'advert_category',
                  'rooms', 'price', 'area',
                  'year', 'building_type',
                  'description']
