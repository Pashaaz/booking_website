from django.db import transaction
from rest_framework import serializers, exceptions
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

    @transaction.atomic
    def create(self, validated_data):
        company = validated_data.pop('company', None)

        try:
            company = Companies.objects.create(**company)

        except (ValueError, TypeError):
            raise exceptions.ValidationError('Invalid data!')

        flight = Flight.objects.create(company=company, **validated_data)

        return flight
