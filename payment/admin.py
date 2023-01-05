from django.contrib import admin

from .models import *

admin.site.register(HotelRoomPrice)
admin.site.register(FlightPrice)
admin.site.register(HotelRoomPaymentLog)
admin.site.register(FlightPaymentLog)
