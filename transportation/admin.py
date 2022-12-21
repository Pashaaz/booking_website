from django.contrib import admin

from transportation.models import *


# Inlines ...
class CompanyInline(admin.TabularInline):
    model = Companies
    extra = 2


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'id')


class FlightAdmin(admin.ModelAdmin):
    search_fields = ('origin', 'destination', 'date', 'flight')
    list_display = ('flight', 'origin', 'destination', 'company')

    # inlines = (CompanyInline,)
    # exclude = ('company',)


admin.site.register(Flight, FlightAdmin)
admin.site.register(Companies, CompanyAdmin)
