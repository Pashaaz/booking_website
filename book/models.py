from django.db import models

from users.models import CustomUser
from residence.models import HotelRoom
from transportation.models import Flight


# -------------------------------------------- Abstract models ---------------------------------------------------------

class AbstractBooking(models.Model):
    STATUS_CHOICES = (
        (1, 'registered'),
        (2, 'approved'),
        (3, 'disapproved'),
        (4, 'cancelled'),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    booked_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    class Meta:
        abstract = True


# ---------------------------------------- End of abstract models ------------------------------------------------------

# ---------------------------------------------- Main models -----------------------------------------------------------

class HotelRoomBooking(AbstractBooking):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_hotel_rooms')
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='room_bookings')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    # booked_days_number = models.DurationField()

    def get_total_price(self):
        pass

    def is_available(self):
        queryset = HotelRoomBooking.objects.all().filter(hotel_room=self['hotel_room'])
        is_available = True

        for item in queryset:
            if self['start_date'] <= item.start_date <= self['end_date']:
                is_available = False

            elif self['start_date'] <= item.end_date <= self['end_date']:
                is_available = False

            elif self['start_date'] >= item.start_date and self['end_date'] <= item.end_date:
                is_available = False

        return is_available


class FlightBooking(AbstractBooking):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='user_flights')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_bookings')
    is_valid = models.BooleanField(default=True)

    def available_number(self):
        flight_capacity = Flight.objects.get(id=self['flight'].id).capacity
        booked_number = FlightBooking.objects.all().filter(flight_id=self['flight'].id, is_valid=True).count()

        available_number = flight_capacity - booked_number

        return available_number

# --------------------------------------------- End of main models -----------------------------------------------------
