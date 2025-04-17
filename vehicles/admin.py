from django.contrib import admin
from vehicles.models import VehicleType, Vehicle


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color', 'owner']
    search_fields = ['license_plate', 'brand', 'model', 'owner']
    list_filter = ['vehicle_type']
