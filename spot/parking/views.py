from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

# Replace Book with ParkingSlot model
from parking.models import ParkingSlot

class ParkingSlotForm(ModelForm):
    class Meta:
        model = ParkingSlot
        fields = ['slot_number', 'is_occupied', 'vehicle_number']

def parking_slot_list(request, template_name='parking/parking_slot_list.html'):
    slots = ParkingSlot.objects.all()
    data = {'object_list': slots}
    return render(request, template_name, data)

def parking_slot_view(request, pk, template_name='parking/parking_slot_detail.html'):
    slot = get_object_or_404(ParkingSlot, pk=pk)
    return render(request, template_name, {'object': slot})

def parking_slot_create(request, template_name='parking/parking_form.html'):
    form = ParkingSlotForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parking_list')
    return render(request, template_name, {'form': form})

def parking_slot_update(request, pk, template_name='parking/parking_form.html'):
    slot = get_object_or_404(ParkingSlot, pk=pk)
    form = ParkingSlotForm(request.POST or None, instance=slot)
    if form.is_valid():
        form.save()
        return redirect('parking_list')
    return render(request, template_name, {'form': form})

def parking_slot_delete(request, pk, template_name='parking/parking_confirm_delete.html'):
    slot = get_object_or_404(ParkingSlot, pk=pk)
    if request.method == 'POST':
        slot.delete()
        return redirect('parking_list')
    return render(request, template_name, {'object': slot})
