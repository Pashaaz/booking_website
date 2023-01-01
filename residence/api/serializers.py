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
    location = LocationSerializer()
    photos = HotelAvatarSerializer(many=True)

    class Meta:
        model = Hotels
        fields = ('title', 'description', 'photos', 'location')


class HotelRoomSerializer(serializers.ModelSerializer):
    facilities = FacilitySerializer(many=True)
    hotel = HotelSerializer()
    photos = HotelRoomAvatarSerializer(many=True)

    class Meta:
        model = HotelRoom
        fields = ('title', 'description', 'price', 'capacity', 'room_number', 'facilities', 'hotel', 'photos')
