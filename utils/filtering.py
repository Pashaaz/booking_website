from django_filters import rest_framework as filters

from residence.models import Hotels, HotelRoom
from transportation.models import Flight
from book.models import HotelRoomBooking, FlightBooking


class HotelFilter(filters.FilterSet):
    class Meta:
        model = Hotels
        fields = {
            # 'title': 'exact',
        }


class HotelRoomFilter(filters.FilterSet):
    class Meta:
        model = HotelRoom
        fields = {
            'title': '',
            # 'payment': ['gte', 'lte'],
            'capacity': ['exact', 'gte', 'lte'],
            'facilities__title': '',
            'hotel__title': '',
        }


class FlightFilter(filters.FilterSet):
    class Meta:
        model = Flight
        fields = {
            # 'company__title': 'exact',
            'origin': '',
            'destination': '',
            'date': '',
            # 'flight_type': '',
        }


class HotelRoomBookingFilter(filters.FilterSet):
    class Meta:
        model = HotelRoomBooking
        fields = {
            'hotel_room__id': '',
            'start_date': ['gte', 'lte'],
            'end_date': ['gte', 'lte'],
        }
