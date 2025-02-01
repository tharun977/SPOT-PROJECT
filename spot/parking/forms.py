from django import forms 
from django.contrib.auth.models import User, Group
from .models import User, VehicleType, ParkingLot, ParkingPlace, ParkingDetail, PaymentDetail, LogDetail


class UserForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'mobile_number', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            self.save_m2m()  # Save the roles (groups)
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
