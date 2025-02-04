from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import login, authenticate

from .models import (
    User, ParkingPlace, ParkingLot, PaymentDetail, VehicleType, 
    LogDetail, Profile
)
from .forms import (
    UserForm, ParkingPlaceForm, ParkingLotForm, PaymentDetailForm, 
    VehicleTypeForm, LogDetailForm, UserRegistrationForm, CustomLoginForm
)

# Helper function to check admin role
def is_admin(user):
    return user.is_authenticated and user.profile.role == "Admin"


# ------------------ Authentication Views ------------------

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role=form.cleaned_data['role'])
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Ensure profile exists
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)  # Create profile if missing

            return redirect("homepage")  # Redirect to homepage after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


@login_required
def homepage(request):
    context = {
        'total_users': User.objects.count(),
        'total_payments': PaymentDetail.objects.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0,
        'total_vehicles': VehicleType.objects.count(),
    }
    return render(request, 'homepage.html', context)


# ------------------ User Management Views ------------------

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'object_list': users})


@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            user.groups.set(form.cleaned_data['roles'])
            messages.success(request, "User created successfully!")
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


@user_passes_test(is_admin)
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


@user_passes_test(is_admin)
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})


# ------------------ Parking Place Views ------------------

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
    if request.method == 'POST':
        form = ParkingPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parking Place added successfully!")
            return redirect('parking_place_list')
    else:
        form = ParkingPlaceForm()
    return render(request, 'parking/parking_place_form.html', {'form': form})


@user_passes_test(is_admin)
def parking_place_delete(request, pk):
    place = get_object_or_404(ParkingPlace, pk=pk)
    if request.method == 'POST':
        place.delete()
        messages.success(request, "Parking Place deleted successfully!")
        return redirect('parking_place_list')
    return render(request, 'parking/parking_place_confirm_delete.html', {'object': place})


# ------------------ Parking Lot Views ------------------

@login_required
def parking_lot_list(request):
    lots = ParkingLot.objects.all()
    return render(request, 'parking/parking_lot_list.html', {'object_list': lots})


@user_passes_test(is_admin)
def parking_lot_create(request):
    if request.method == 'POST':
        form = ParkingLotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parking Lot added successfully!")
            return redirect('parking_lot_list')
    else:
        form = ParkingLotForm()
    return render(request, 'parking/parking_lot_form.html', {'form': form})


@user_passes_test(is_admin)
def parking_lot_update(request, pk):
    lot = get_object_or_404(ParkingLot, pk=pk)
    if request.method == 'POST':
        form = ParkingLotForm(request.POST, instance=lot)
        if form.is_valid():
            form.save()
            messages.success(request, "Parking Lot updated successfully!")
            return redirect('parking_lot_list')
    else:
        form = ParkingLotForm(instance=lot)
    return render(request, 'parking/parking_lot_form.html', {'form': form})


@user_passes_test(is_admin)
def parking_lot_delete(request, pk):
    lot = get_object_or_404(ParkingLot, pk=pk)
    if request.method == 'POST':
        lot.delete()
        messages.success(request, "Parking Lot deleted successfully!")
        return redirect('parking_lot_list')
    return render(request, 'parking/parking_lot_confirm_delete.html', {'object': lot})


# ------------------ Payment Details Views ------------------

@login_required
def payment_detail_list(request):
    payments = PaymentDetail.objects.all()
    return render(request, 'parking/payment_detail_list.html', {'object_list': payments})


@login_required
def payment_detail_view(request, pk):
    payment = get_object_or_404(PaymentDetail, pk=pk)
    return render(request, 'parking/payment_detail_view.html', {'object': payment})


# ------------------ Vehicle Type Views ------------------

@login_required
def vehicle_type_list(request):
    vehicle_types = VehicleType.objects.all()
    return render(request, 'parking/vehicle_type_list.html', {'object_list': vehicle_types})


@user_passes_test(is_admin)
def vehicle_type_create(request):
    form = VehicleTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_type_list')
    return render(request, 'parking/vehicle_type_form.html', {'form': form})


@user_passes_test(is_admin)
def vehicle_type_delete(request, pk):
    vehicle_type = get_object_or_404(VehicleType, pk=pk)
    vehicle_type.delete()
    return redirect('vehicle_type_list')


# ------------------ Log Details Views ------------------

@login_required
def log_detail_list(request):
    logs = LogDetail.objects.all()
    return render(request, 'parking/log_detail_list.html', {'object_list': logs})


@login_required
def log_detail_view(request, pk):
    log = get_object_or_404(LogDetail, pk=pk)
    return render(request, 'parking/log_detail_view.html', {'object': log})
