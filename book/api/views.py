from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from django_filters import rest_framework as filters

from book.api.serializers import HotelRoomBookingSerializer, FlightBookingSerializer
from book.models import HotelRoomBooking, FlightBooking
from transportation.models import Flight
from utils.filtering import HotelRoomBookingFilter


class HotelRoomSearchBookedViewSet(mixins.ListModelMixin,
                                   viewsets.GenericViewSet):

    serializer_class = HotelRoomBookingSerializer
    queryset = HotelRoomBooking.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelRoomBookingFilter


class FlightAvailableNumber(APIView):

    def get(self, request):
        flight_booking_object = FlightBooking.objects.get(flight_id=request.data.get('id'))
        available = FlightBooking.available_number(flight_booking_object)

        return Response({'available': available})


class HotelRoomBookingViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    queryset = HotelRoomBooking.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelRoomBookingSerializer

    def get_permissions(self):
        if self.action in ['list']:
            return [IsAdminUser()]

        elif self.action in ['create']:
            return [IsAuthenticated()]


class FlightBookingViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = FlightBooking.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = FlightBookingSerializer

    def get_permissions(self):
        if self.action in ['list']:
            return [IsAdminUser()]

        elif self.action in ['create']:
            return [IsAuthenticated()]
