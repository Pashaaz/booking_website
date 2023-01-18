from django.db import transaction
from rest_framework import serializers, exceptions

from payment.api.serializers import HotelRoomCurrencySerializer
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
        fields = ('id', 'title', 'description', 'photos', 'location')

    @transaction.atomic
    def create(self, validated_data):
        location = validated_data.pop('location', None)
        photos = validated_data.pop('photos', None)

        try:
            location = Locations.objects.get_or_create(**location)
            HotelAvatar.objects.get_or_create(all(photos))

        except (ValueError, TypeError):
            raise exceptions.ValidationError('Invalid data!')

        hotel = Hotels.objects.create(location=location, **validated_data)

        return hotel


class HotelRoomSerializer(serializers.ModelSerializer):
    facilities = FacilitySerializer(many=True)
    hotel = HotelSerializer()
    photos = HotelRoomAvatarSerializer(many=True)
    hotel_room_prices = HotelRoomCurrencySerializer()

    class Meta:
        model = HotelRoom
        fields = ('id', 'title', 'description',
                  'capacity', 'room_number', 'facilities',
                  'hotel', 'photos', 'hotel_room_prices')

    @transaction.atomic
    def create(self, validated_data):
        hotel = validated_data.pop('hotel', None)
        photos = validated_data.pop('photos', None)
        facilities = validated_data('facilities', None)

        try:
            hotel = Hotels.objects.get_or_create(**hotel)
            HotelRoomAvatar.objects.get_or_create(all(**photos))
            Facilities.objects.get_or_create(all(**photos))

        except (ValueError, TypeError):
            raise exceptions.ValidationError('Invalid data!')

        room = HotelRoom.objects.create(hotel=hotel, facilities=facilities, **validated_data)

        return room
