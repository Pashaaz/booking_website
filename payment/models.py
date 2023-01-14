from django.db import models

from book.models import HotelRoomBooking, FlightBooking
from residence.models import HotelRoom
from transportation.models import Flight
from users.models import CustomUser


class AbstractPrice(models.Model):
    price = models.IntegerField()

    class Meta:
        abstract = True


class AbstractPaymentLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Currency(models.Model):
    iri_to = models.CharField(max_length=3)
    ratio = models.IntegerField()


class HotelRoomPrice(AbstractPrice):
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE,
                                   related_name='hotel_room_prices')


class FlightPrice(AbstractPrice):
    TYPE_CHOICES = (
        (1, 'Economy'),
        (2, 'Business'),
        (3, 'First_Class'),
    )

    flight_type = models.SmallIntegerField(choices=TYPE_CHOICES)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,
                               related_name='flight_prices')


class HotelRoomPaymentLog(AbstractPaymentLog):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_room_payments')
    booking_obj = models.ForeignKey(HotelRoomBooking, on_delete=models.DO_NOTHING, related_name='room_payments')


class FlightPaymentLog(AbstractPaymentLog):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_flight_payments')
    booking_obj = models.ForeignKey(FlightBooking, on_delete=models.DO_NOTHING, related_name='flight_payments')
