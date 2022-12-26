from rest_framework import serializers
from residence.models import *


class HotelAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAvatar
        fields = ('image',)


class HotelRoomAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomAvatar
        fields = ('image',)


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('title',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('address', 'map_link')


class HotelSerializer(serializers.ModelSerializer):
    # hotel_locations = LocationSerializer(many=True)
    photos = HotelAvatarSerializer(many=True)

    class Meta:
        model = Hotels
        fields = ('title', 'description', 'photos')


class HotelRoomSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer(many=True)
    hotel = HotelSerializer()
    # image = HotelRoomAvatarSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'price', 'capacity', 'room_number', 'facility', 'hotel')
