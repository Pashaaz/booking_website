from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from book.api.serializers import HotelRoomBookingSerializer, FlightBookingSerializer
from book.models import HotelRoomBooking, FlightBooking


class HotelRoomBookingViewSet(mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):

    queryset = HotelRoomBooking.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = HotelRoomBookingSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            return [IsAdminUser()]

        elif self.action in ['create', 'update']:
            return [IsAuthenticated()]

