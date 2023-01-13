from rest_framework import serializers

from payment.models import (
    FlightPaymentLog,
    HotelRoomPaymentLog,
    HotelRoomPrice,
    FlightPrice
)


class FlightPaymentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPaymentLog
        fields = ('id', 'user', 'date', 'status', 'booking_obj')


class HotelRoomPaymentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomPaymentLog
        fields = ('id', 'user', 'date', 'status', 'booking_obj')


class HotelRoomPriceSerializer(serializers.ModelSerializer):
    iri_to = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = HotelRoomPrice
        fields = ('id', 'price', 'hotel_room', 'iri_to')


class FlightPriceSerializer(serializers.ModelSerializer):
    iri_to = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = FlightPrice
        fields = ('id', 'price', 'flight', 'iri_to')
