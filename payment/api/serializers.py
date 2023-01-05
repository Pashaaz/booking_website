from rest_framework import serializers

from payment.models import FlightPaymentLog, HotelRoomPaymentLog


class FlightPaymentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPaymentLog
        fields = ('id', 'user', 'date', 'status', 'booking_obj')


class HotelRoomPaymentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomPaymentLog
        fields = ('id', 'user', 'date', 'status', 'booking_obj')
