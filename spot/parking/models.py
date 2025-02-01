from django.db import models


class User(models.Model):
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
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)  # Using choices for the role


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
    lot_id = models.AutoField(primary_key=True)
    parking_id = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE)
    status_before = models.BooleanField(default=False)
    status_after = models.BooleanField(default=False)

    def __str__(self):
        return f"Lot {self.lot_id} in {self.parking_id.place_name}"


class ParkingDetail(models.Model):
    parking_id = models.AutoField(primary_key=True)
    place_id = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE)
    lot_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    parking_duration = models.DurationField()
    occupied_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Parking {self.parking_id} - Vehicle: {self.vehicle_type_id}"


class PaymentDetail(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_id = models.ForeignKey(ParkingDetail, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment {self.payment_id} by {self.user_id.username}"


class LogDetail(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Log {self.log_id} by {self.user_id.username}"
