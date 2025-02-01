from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from parking.models import ParkingPlace, ParkingLot, PaymentDetail, VehicleType, LogDetail, User
from .forms import UserForm

def homepage(request):
    return render(request, 'base.html')  # Make sure 'homepage.html' exists in your templates


# Form Classes
class ParkingPlaceForm(ModelForm):
    class Meta:
        model = ParkingPlace
        fields = ['place_name', 'location', 'capacity', 'status']

class ParkingLotForm(ModelForm):
    class Meta:
        model = ParkingLot
        fields = ['parking_id', 'status_before', 'status_after']

class PaymentDetailForm(ModelForm):
    class Meta:
        model = PaymentDetail
        fields = ['user_id', 'parking_id', 'amount_paid', 'payment_method', 'payment_date', 'payment_status']

class VehicleTypeForm(ModelForm):
    class Meta:
        model = VehicleType
        fields = ['vehicle_type_id', 'vehicle_reg_no', 'vehicle_type']

class LogDetailForm(ModelForm):
    class Meta:
        model = LogDetail
        fields = ['user_id', 'timestamp']

# Parking Place Views
def parking_place_list(request, template_name='parking/parking_place_list.html'):
    places = ParkingPlace.objects.all()
    data = {'object_list': places}
    return render(request, template_name, data)

def parking_place_view(request, pk, template_name='parking/parking_place_detail.html'):
    place = get_object_or_404(ParkingPlace, pk=pk)
    return render(request, template_name, {'object': place})

def parking_place_create(request, template_name='parking/parking_place_form.html'):
    form = ParkingPlaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parking_place_list')
    return render(request, template_name, {'form': form})

def parking_place_update(request, pk, template_name='parking/parking_place_form.html'):
    place = get_object_or_404(ParkingPlace, pk=pk)
    form = ParkingPlaceForm(request.POST or None, instance=place)
    if form.is_valid():
        form.save()
        return redirect('parking_place_list')
    return render(request, template_name, {'form': form})

def parking_place_delete(request, pk, template_name='parking/parking_place_confirm_delete.html'):
    place = get_object_or_404(ParkingPlace, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('parking_place_list')
    return render(request, template_name, {'object': place})

# Payment Detail Views
def payment_detail_list(request, template_name='parking/payment_detail_list.html'):
    payments = PaymentDetail.objects.all()
    data = {'object_list': payments}
    return render(request, template_name, data)

def payment_detail_view(request, pk, template_name='parking/payment_detail_view.html'):
    payment = get_object_or_404(PaymentDetail, pk=pk)
    return render(request, template_name, {'object': payment})

def payment_detail_create(request, template_name='parking/payment_detail_form.html'):
    form = PaymentDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('payment_detail_list')
    return render(request, template_name, {'form': form})

def payment_detail_update(request, pk, template_name='parking/payment_detail_form.html'):
    payment = get_object_or_404(PaymentDetail, pk=pk)
    form = PaymentDetailForm(request.POST or None, instance=payment)
    if form.is_valid():
        form.save()
        return redirect('payment_detail_list')
    return render(request, template_name, {'form': form})

def payment_detail_delete(request, pk, template_name='parking/payment_detail_confirm_delete.html'):
    payment = get_object_or_404(PaymentDetail, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_detail_list')
    return render(request, template_name, {'object': payment})

# Vehicle Type Views
def vehicle_type_list(request, template_name='parking/vehicle_type_list.html'):
    vehicle_types = VehicleType.objects.all()
    data = {'object_list': vehicle_types}
    return render(request, template_name, data)

def vehicle_type_view(request, pk, template_name='parking/vehicle_type_view.html'):
    vehicle_type = get_object_or_404(VehicleType, pk=pk)
    return render(request, template_name, {'object': vehicle_type})

def vehicle_type_create(request, template_name='parking/vehicle_type_form.html'):
    form = VehicleTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_type_list')
    return render(request, template_name, {'form': form})

def vehicle_type_update(request, pk, template_name='parking/vehicle_type_form.html'):
    vehicle_type = get_object_or_404(VehicleType, pk=pk)
    form = VehicleTypeForm(request.POST or None, instance=vehicle_type)
    if form.is_valid():
        form.save()
        return redirect('vehicle_type_list')
    return render(request, template_name, {'form': form})

def vehicle_type_delete(request, pk, template_name='parking/vehicle_type_confirm_delete.html'):
    vehicle_type = get_object_or_404(VehicleType, pk=pk)
    if request.method == 'POST':
        vehicle_type.delete()
        return redirect('vehicle_type_list')
    return render(request, template_name, {'object': vehicle_type})

# Log Detail Views
def log_detail_list(request, template_name='parking/log_detail_list.html'):
    logs = LogDetail.objects.all()
    data = {'object_list': logs}
    return render(request, template_name, data)

def log_detail_view(request, pk, template_name='parking/log_detail_view.html'):
    log = get_object_or_404(LogDetail, pk=pk)
    return render(request, template_name, {'object': log})

def log_detail_create(request, template_name='parking/log_detail_form.html'):
    form = LogDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('log_detail_list')
    return render(request, template_name, {'form': form})

def log_detail_update(request, pk, template_name='parking/log_detail_form.html'):
    log = get_object_or_404(LogDetail, pk=pk)
    form = LogDetailForm(request.POST or None, instance=log)
    if form.is_valid():
        form.save()
        return redirect('log_detail_list')
    return render(request, template_name, {'form': form})

def log_detail_delete(request, pk, template_name='parking/log_detail_confirm_delete.html'):
    log = get_object_or_404(LogDetail, pk=pk)
    if request.method == 'POST':
        log.delete()
        return redirect('log_detail_list')
    return render(request, template_name, {'object': log})

# User Views
def user_list(request, template_name='parking/user_list.html'):
    users = User.objects.all()
    data = {'object_list': users}
    return render(request, template_name, data)

def user_view(request, pk, template_name='parking/user_detail.html'):
    user = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'user': user})

def user_create(request, template_name='parking/user_form.html'):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Replace 'user_list' with your actual user list view name
    else:
        form = UserForm()
    return render(request, template_name, {'form': form})

def user_update(request, pk, template_name='parking/user_form.html'):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)  # Replace 'user_detail' with the correct URL name
    else:
        form = UserForm(instance=user)
    return render(request, template_name, {'form': form})

def user_delete(request, pk, template_name='parking/user_confirm_delete.html'):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Replace with the actual name of the user list view
    return render(request, template_name, {'user': user})
