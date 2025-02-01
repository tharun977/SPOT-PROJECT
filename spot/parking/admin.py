from django.contrib import admin
from .models import User, VehicleType, ParkingPlace, ParkingLot, ParkingDetail, PaymentDetail, LogDetail

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'full_name', 'mobile_number', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)  # Filter by role (Admin, Staff, User)

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type_id', 'vehicle_type', 'vehicle_reg_no')
    search_fields = ('vehicle_type', 'vehicle_reg_no')

@admin.register(ParkingPlace)
class ParkingPlaceAdmin(admin.ModelAdmin):
    list_display = ('place_id', 'place_name', 'location', 'capacity', 'status')
    list_filter = ('status',)
    search_fields = ('place_name',)

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display = ('lot_id', 'parking_id', 'status_before', 'status_after')
    list_filter = ('status_before', 'status_after')
    search_fields = ('lot_id',)

@admin.register(ParkingDetail)
class ParkingDetailAdmin(admin.ModelAdmin):
    list_display = ('parking_id', 'place_id', 'lot_id', 'vehicle_type_id', 'in_time', 'out_time', 'parking_duration')
    list_filter = ('in_time', 'out_time')
    search_fields = ('parking_id',)

@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'user_id', 'parking_id', 'amount_paid', 'payment_method', 'payment_status')
    list_filter = ('payment_status', 'payment_method')
    search_fields = ('payment_id',)

@admin.register(LogDetail)
class LogDetailAdmin(admin.ModelAdmin):
    list_display = ('log_id', 'user_id', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('log_id',)
