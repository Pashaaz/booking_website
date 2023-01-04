from django.urls import path
from rest_framework.routers import DefaultRouter

from book.api.views import (HotelRoomBookingViewSet,
                            FlightBookingViewSet,
                            HotelRoomSearchBookedViewSet,
                            FlightAvailableNumber,
                            )

router = DefaultRouter()

router.register(r'book/hotelroom', HotelRoomBookingViewSet, basename='bookhotelroom')
router.register(r'book/flight', FlightBookingViewSet, basename='bookflight')
router.register(r'search/booked/hotelrooms', HotelRoomSearchBookedViewSet, basename='searchbookedhotelrooms')

urlpatterns = [
    path('search/avnum/flight/', FlightAvailableNumber.as_view(), name='searchavnumflight'),
]

urlpatterns += router.urls
