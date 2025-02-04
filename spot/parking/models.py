from django.db import models
from django.contrib.auth.models import User



class CustomUser(models.Model):  
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('User', 'User'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('User', 'User')])

    def __str__(self):
        return self.user.username


class VehicleType(models.Model):
    vehicle_type_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)
    vehicle_reg_no = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_type


class ParkingPlace(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.place_name


class ParkingLot(models.Model):
    name = models.CharField(max_length=255)  # ✅ Ensure this exists
    location = models.CharField(max_length=255)  # ✅ Ensure this exists
    capacity = models.IntegerField()  # ✅ Ensure this exists

    def __str__(self):
        return self.name
    
    
class ParkingDetail(models.Model):
    parking_id = models.AutoField(primary_key=True)
    place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE)
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    in_time = models.DateTimeField()
    out_time = models.DateTimeField(null=True, blank=True)
    parking_duration = models.DurationField(null=True, blank=True)
    occupied_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Parking {self.parking_id} - Vehicle: {self.vehicle_type}"


class PaymentDetail(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking = models.ForeignKey(ParkingDetail, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment {self.payment_id} by {self.user.username}"


class LogDetail(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.log_id} by {self.user.username}"
