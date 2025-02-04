from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, VehicleType, ParkingLot, ParkingPlace, ParkingDetail, PaymentDetail, LogDetail


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Change from User to CustomUser
        fields = ['username', 'full_name', 'mobile_number', 'email', 'password1', 'password2']



# Custom Login Form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Change from User to CustomUser
        fields = ['username', 'full_name', 'mobile_number', 'email', 'role']
        
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password"])  # Hash password
            user.save()
            self.save_m2m()  # Save many-to-many relationship (roles)
            user.groups.set(self.cleaned_data['roles'])  # Assign the roles
        return user


# Vehicle Type Form
class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['vehicle_type', 'vehicle_reg_no']


# Parking Place Form
class ParkingPlaceForm(forms.ModelForm):
    class Meta:
        model = ParkingPlace
        fields = ['place_name', 'location', 'capacity', 'status']


# Parking Lot Form
class ParkingLotForm(forms.ModelForm):
    class Meta:
        model = ParkingLot  # ✅ Ensure this matches your actual model name
        fields = ['name', 'location', 'capacity']  # ❌ Remove 'parking_id' if it's auto-generated
        

# Parking Detail Form
class ParkingDetailForm(forms.ModelForm):
    class Meta:
        model = ParkingDetail
        fields = ['place_id', 'lot_id', 'vehicle_type_id', 'in_time', 'out_time', 'parking_duration', 'occupied_by']


# Payment Detail Form
class PaymentDetailForm(forms.ModelForm):
    class Meta:
        model = PaymentDetail
        fields = ['user_id', 'parking_id', 'amount_paid', 'payment_method', 'payment_date', 'payment_status']


# Log Detail Form
class LogDetailForm(forms.ModelForm):
    class Meta:
        model = LogDetail
        fields = ['user_id', 'timestamp']
