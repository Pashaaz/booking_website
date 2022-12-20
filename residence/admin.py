from django.contrib import admin

from residence.models import *


# Inlines ...
class HotelInline(admin.TabularInline):
    model = Hotels
    extra = 2


class HotelAvatarInline(admin.TabularInline):
    model = HotelAvatar
    extra = 3


class HotelRoomAvatarInline(admin.TabularInline):
    model = HotelRoom
    extra = 4


class LocationsInline(admin.TabularInline):
    model = Locations
    extra = 2


class FacilitiesInline(admin.TabularInline):
    model = Facilities
    extra = 2


# End of Inlines.

# Admin classes ...
class HotelAvatarAdmin(admin.ModelAdmin):
    pass


class HotelRoomAvatarAdmin(admin.ModelAdmin):
    pass


class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('address',)
    search_fields = ('address', 'map_link')


class HotelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

    # inlines = (HotelAvatarInline, LocationsInline)


class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number',)
    search_fields = ('hotel', 'room_number')

    # inlines = (HotelInline, HotelRoomAvatarInline, FacilitiesInline)


# End of Admin classes.


# Registrations

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(HotelRoom, HotelRoomAdmin)
admin.site.register(Facilities, FacilitiesAdmin)
admin.site.register(Locations, LocationAdmin)
admin.site.register(HotelAvatar, HotelAvatarAdmin)
admin.site.register(HotelRoomAvatar, HotelRoomAvatarAdmin)
