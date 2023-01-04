from rest_framework import viewsets, mixins
from residence.api.serializers import HotelSerializer, HotelRoomSerializer
from residence.models import Hotels, HotelRoom

from django_filters import rest_framework as filters

from utils.filtering import HotelFilter, HotelRoomFilter


class HotelsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelFilter


class HotelRoomViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):

    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelRoomFilter
