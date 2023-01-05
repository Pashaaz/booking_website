from django.urls import path
from rest_framework.routers import DefaultRouter

from book.api.views import (HotelRoomBookingViewSet,
                            FlightBookingViewSet,
                            HotelRoomSearchBookedViewSet,
                            FlightAvailableNumber,
                            )

router = DefaultRouter()

router.register(r'hotelroom', HotelRoomBookingViewSet, basename='hotelroom')
router.register(r'flight', FlightBookingViewSet, basename='flight')
router.register(r'search/booked/hotelrooms', HotelRoomSearchBookedViewSet, basename='searchbookedhotelrooms')

urlpatterns = [
    path('search/avnum/flight/', FlightAvailableNumber.as_view(), name='searchavnumflight'),
]

urlpatterns += router.urls
