from django.contrib import admin
from .models import ParkingSlot

@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_number', 'is_occupied', 'vehicle_number', 'parked_at', 'updated_at')
    list_filter = ('is_occupied',)
    search_fields = ('slot_number', 'vehicle_number')

