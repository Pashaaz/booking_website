from rest_framework import viewsets, mixins
from transportation.api.serializers import CompanySerializer, FlightSerializer
from transportation.models import Companies, Flight

from django_filters import rest_framework as filters

from utils.filtering import FlightFilter


class FlightViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightFilter
