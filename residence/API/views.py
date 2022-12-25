from rest_framework import viewsets, mixins
from residence.API.serializers import HotelSerializer
from residence.models import Hotels, HotelRoom


class HotelsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Hotels.objects.all()

    serializer_class = HotelSerializer
