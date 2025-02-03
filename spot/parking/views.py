from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Sum
from .models import User, ParkingPlace, ParkingLot, PaymentDetail, VehicleType, LogDetail
from .forms import UserForm, ParkingPlaceForm, ParkingLot, PaymentDetailForm, VehicleTypeForm, LogDetailForm
from django.forms import ModelForm


def is_admin(user):
    return user.is_authenticated and user.role == "Admin"

# Homepage Dashboard View
@login_required
def homepage(request):
    total_users = User.objects.count()
    total_payments = PaymentDetail.objects.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
    total_vehicles = VehicleType.objects.count()
    
    context = {
        'total_users': total_users,
        'total_payments': total_payments,
        'total_vehicles': total_vehicles,
    }
    return render(request, 'homepage.html', context)  # Return context in response

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

# User Views
@login_required
def user_list(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'users/user_list.html', {'object_list': users})

@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Secure password
            user.save()
            user.groups.set(form.cleaned_data['roles'])  # Assign roles
            messages.success(request, "User created successfully!")
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

@user_passes_test(is_admin)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

@user_passes_test(is_admin)
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_view', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


# Parking Place Views
@login_required
def parking_place_list(request):
    places = ParkingPlace.objects.all()
    return render(request, 'parking/parking_place_list.html', {'object_list': places})

@login_required
def parking_place_view(request, pk):
    place = get_object_or_404(ParkingPlace, pk=pk)
    return render(request, 'parking/parking_place_detail.html', {'object': place})

@user_passes_test(is_admin)
def parking_place_create(request):
    form = ParkingPlaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Parking Place added successfully!")
        return redirect('parking_place_list')
    return render(request, 'parking/parking_place_form.html', {'form': form})

@user_passes_test(is_admin)
def parking_place_delete(request, pk):
    place = get_object_or_404(ParkingPlace, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('parking_place_list')
    return render(request, 'parking/parking_place_confirm_delete.html', {'object': place})

# Parking Lot Views (Admin Only)
@user_passes_test(is_admin)
def parking_lot_create(request):
    form = ParkingLotForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Parking Lot added successfully!")
        return redirect('parking_place_list')
    return render(request, 'parking/parking_lot_form.html', {'form': form})


# Payment Detail Views
@login_required
def payment_detail_list(request):
    payments = PaymentDetail.objects.all()
    return render(request, 'parking/payment_detail_list.html', {'object_list': payments})

# Vehicle Type Views
@login_required
def vehicle_type_list(request):
    vehicle_types = VehicleType.objects.all()
    return render(request, 'parking/vehicle_type_list.html', {'object_list': vehicle_types})

# Log Detail Views
@login_required
def log_detail_list(request):
    logs = LogDetail.objects.all()
    return render(request, 'parking/log_detail_list.html', {'object_list': logs})
