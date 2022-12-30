from rest_framework import viewsets, mixins
from transportation.API.serializers import CompanySerializer, FlightSerializer
from transportation.models import Companies, Flight


class FlightViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
