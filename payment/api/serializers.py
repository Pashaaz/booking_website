from rest_framework import serializers

from payment.models import (
    FlightPaymentLog,
    HotelRoomPaymentLog,
    HotelRoomPrice,
    FlightPrice,
    Currency,
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
    class Meta:
        model = HotelRoomPrice
        fields = ('id', 'price', 'hotel_room')


class FlightPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPrice
        fields = ('id', 'price', 'flight')


class HotelRoomCurrencySerializer(serializers.ModelSerializer):
    iri_to = serializers.CharField(max_length=3, required=False)

    class Meta:
        model = HotelRoomPrice
        fields = ('id', 'price', 'hotel_room', 'iri_to')

    def to_representation(self, instance):
        if self['iri_to']:
            currency = Currency.objects.get(iri_to=self['iri_to'])
            price = int(self['price']) * currency.ratio

            self['price'] = price

        super(HotelRoomCurrencySerializer, self).to_representation(self)


class FlightCurrencySerializer(serializers.ModelSerializer):
    iri_to = serializers.CharField(max_length=3, required=False)

    class Meta:
        model = FlightPrice
        fields = ('id', 'price', 'flight', 'iri_to')

    def to_representation(self, instance):
        if self['iri_to']:
            currency = Currency.objects.get(iri_to=self['iri_to'])
            price = int(self['price']) * currency.ratio

            self['price'] = price

        super(FlightCurrencySerializer, self).to_representation(self)
