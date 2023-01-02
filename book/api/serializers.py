from rest_framework import serializers

from book.models import HotelRoomBooking, FlightBooking


class HotelRoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomBooking
        fields = ('__all__',)


class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBooking
        fields = ('__all__',)
