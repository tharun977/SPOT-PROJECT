from django.db import models
from django.urls import reverse

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=50, unique=True)
    is_occupied = models.BooleanField(default=False)
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)
    parked_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slot {self.slot_number} - {'Occupied' if self.is_occupied else 'Available'}"

    def get_absolute_url(self):
        return reverse('parking_slot_edit', kwargs={'pk': self.pk})
