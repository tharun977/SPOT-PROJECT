from django import forms 
from django.contrib.auth.models import User, Group
from .models import User, VehicleType, ParkingLot, ParkingPlace, ParkingDetail, PaymentDetail, LogDetail
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    mobile_number = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'full_name', 'mobile_number', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'mobile_number', 'email', 'roles']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password"])  # Hash password
            user.save()
            self.save_m2m()  # Save the many-to-many relationship (roles)
            user.groups.set(self.cleaned_data['roles'])  # Assign the roles
        return user
    
    

class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['vehicle_type', 'vehicle_reg_no']


class ParkingPlaceForm(forms.ModelForm):
    class Meta:
        model = ParkingPlace
        fields = ['place_name', 'location', 'capacity', 'status']


class ParkingDetailForm(forms.ModelForm):
    class Meta:
        model = ParkingDetail
        fields = ['place_id', 'lot_id', 'vehicle_type_id', 'in_time', 'out_time', 'parking_duration', 'occupied_by']


class PaymentDetailForm(forms.ModelForm):
    class Meta:
        model = PaymentDetail
        fields = ['user_id', 'parking_id', 'amount_paid', 'payment_method', 'payment_date', 'payment_status']


class LogDetailForm(forms.ModelForm):
    class Meta:
        model = LogDetail
        fields = ['user_id', 'timestamp']
