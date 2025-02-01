from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ParkingSlot

class ParkingSlotList(ListView):
    model = ParkingSlot
    template_name = 'parking/parking_list.html'  # Customize the template path

class ParkingSlotDetail(DetailView):
    model = ParkingSlot
    template_name = 'parking/parking_detail.html'

class ParkingSlotCreate(CreateView):
    model = ParkingSlot
    fields = ['slot_number', 'is_occupied', 'vehicle_number']
    success_url = reverse_lazy('parking_list')

class ParkingSlotUpdate(UpdateView):
    model = ParkingSlot
    fields = ['slot_number', 'is_occupied', 'vehicle_number']
    success_url = reverse_lazy('parking_list')

class ParkingSlotDelete(DeleteView):
    model = ParkingSlot
    success_url = reverse_lazy('parking_list')
