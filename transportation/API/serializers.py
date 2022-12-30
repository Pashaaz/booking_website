from rest_framework import serializers
from transportation.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('title',)


class FlightSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Flight
        fields = ('company', 'origin', 'destination', 'date', 'boarding_till', 'depart_time',
                  'arrive_time', 'ticket_enrollment', 'gate', 'flight',)
