from django.db import models

from residence.models import HotelRoom
from transportation.models import Flight


class AbstractPrice(models.Model):
    price = models.IntegerField()

    class Meta:
        abstract = True


class HotelRoomPrice(AbstractPrice):
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)


class FlightPrice(AbstractPrice):
    TYPE_CHOICES = (
        (1, 'Economy'),
        (2, 'Business'),
        (3, 'First_Class'),
    )

    flight_type = models.SmallIntegerField(choices=TYPE_CHOICES)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
