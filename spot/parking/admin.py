from django.contrib import admin
from .models import CustomUser, VehicleType, ParkingPlace, ParkingLot, ParkingDetail, PaymentDetail, LogDetail

admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'full_name', 'mobile_number', 'email', 'role')

admin.site.register(VehicleType)
admin.site.register(ParkingPlace)
admin.site.register(ParkingLot)
admin.site.register(ParkingDetail)
admin.site.register(PaymentDetail)
admin.site.register(LogDetail)
