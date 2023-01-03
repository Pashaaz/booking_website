from django_filters import rest_framework as filters

from residence.models import Hotels, HotelRoom
from transportation.models import Flight
from book.models import HotelRoomBooking, FlightBooking


class HotelFilter(filters.FilterSet):
    class Meta:
        model = Hotels
        fields = {
            'title': 'exact'
        }


class HotelRoomFilter(filters.FilterSet):
    class Meta:
        model = HotelRoom
        fields = {
            'title': 'exact',
            'price': ['gte', 'lte'],
            'capacity': ['exact', 'gte', 'lte'],
            'facilities__title': 'exact',
            'hotel__title': 'exact',
        }


class FlightFilter(filters.FilterSet):
    class Meta:
        model = Flight
        fields = {
            'company__title': 'exact',
            'origin': 'exact',
            'destination': 'exact',
            'date': 'exact',
            'flight_type': 'exact',
        }


class HotelRoomBookingFilter(filters.FilterSet):
    class Meta:
        model = HotelRoomBooking
        fields = {
            'start_date': ['gte', 'lte'],
            'end_date': ['gte', 'lte'],
        }
