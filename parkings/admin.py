from django.contrib import admin
from parkings.models import ParkingRecord, ParkingSpot


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_empty']
    search_fields = ['spot_number']
    list_filter = ['is_empty']


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number']  #PARKING_SPOT__SPOT_NUM serve para resolver a FK

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parking_spot' and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_empty=True)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
