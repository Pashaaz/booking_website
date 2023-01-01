from rest_framework import viewsets, mixins
from residence.api.serializers import HotelSerializer, HotelRoomSerializer
from residence.models import Hotels, HotelRoom


class HotelsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Hotels.objects.all()

    serializer_class = HotelSerializer


class HotelRoomViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):

    queryset = HotelRoom.objects.all()

    serializer_class = HotelRoomSerializer
