from django.db import models

from users.models import CustomUser
from residence.models import HotelRoom
from transportation.models import Flight


class AbstractBooking(models.Model):
    STATUS_CHOICES = (
        (1, 'registered'),
        (2, 'approved'),
        (3, 'disapproved'),
        (4, 'cancelled'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_bookings')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    booked_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    class Meta:
        abstract = True


class HotelRoomBooking(AbstractBooking):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_hotel_rooms')
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='room_bookings')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    booked_days_number = models.DurationField()

    def get_total_price(self):
        pass


class FlightBooking(AbstractBooking):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_flights')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_bookings')
    is_valid = models.BooleanField(default=True)
