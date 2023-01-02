from rest_framework import serializers

from book.models import HotelRoomBooking, FlightBooking
from users.api.serializers import CustomUserSerializer
from residence.api.serializers import HotelRoomSerializer
from transportation.api.serializers import FlightSerializer


class HotelRoomBookingSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    hotel_room = HotelRoomSerializer()

    class Meta:
        model = HotelRoomBooking
        fields = ('__all__',)


class FlightBookingSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    flight = FlightSerializer()

    class Meta:
        model = FlightBooking
        fields = ('__all__',)
