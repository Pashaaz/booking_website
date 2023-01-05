from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView

from book.models import HotelRoomBooking
from payment.api.serializers import FlightPaymentLogSerializer, HotelRoomPaymentLogSerializer
from payment.models import FlightPaymentLog, HotelRoomPaymentLog


class HotelRoomAfterPaymentAPIView(GenericAPIView):

    serializer_class = HotelRoomPaymentLogSerializer
    queryset = HotelRoomPaymentLog.objects.all()


class FlightAfterPaymentAPIView(GenericAPIView):

    serializer_class = FlightPaymentLogSerializer
    queryset = FlightPaymentLog.objects.all()
