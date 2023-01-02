from rest_framework import serializers, status
from rest_framework.exceptions import NotAcceptable

from book.models import HotelRoomBooking, FlightBooking
from users.api.serializers import CustomUserSerializer
from residence.api.serializers import HotelRoomSerializer
from transportation.api.serializers import FlightSerializer


class HotelRoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomBooking
        fields = ('id', 'status', 'user', 'hotel_room',
                  'start_date', 'end_date', 'booked_days_number')

    def create(self, validated_data):
        if HotelRoomBooking.is_available(self.data):

            super(HotelRoomBookingSerializer, self).create(validated_data)

        else:
            raise NotAcceptable(detail='Can\'t book by this start and end date!', code=status.HTTP_400_BAD_REQUEST)


class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBooking
        fields = ('id', 'status', 'user', 'flight', 'is_valid')

    def create(self, validated_data):
        if FlightBooking.available_number(self.data) > 0:
            super(FlightBookingSerializer, self).create(validated_data)
        else:
            raise NotAcceptable(detail='Flight not available!', code=status.HTTP_400_BAD_REQUEST)
