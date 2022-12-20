from django.contrib import admin

from transportation.models import *


# Inlines ...
class CompanyInline(admin.TabularInline):
    model = Companies
    extra = 2


class FlightAdmin(admin.ModelAdmin):
    search_fields = ('origin', 'destination', 'date', 'flight')
    list_display = ('flight', 'origin', 'destination', 'company')

    inlines = (CompanyInline,)


admin.site.register(Flight)
