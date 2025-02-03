from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # The root URL for homepage
    # User URLs
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_new'),
    path('users/edit/<int:pk>/', views.user_update, name='user_edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('user/create/', views.user_create, name='user_create'),

    
    # ParkingPlace URLs
    path('parking-places/', views.parking_place_list, name='parking_place_list'),
    path('parking-places/create/', views.parking_place_create, name='parking_place_create'),
    path('parking-places/view/<int:pk>/', views.parking_place_view, name='parking_place_view'),
    path('parking-places/delete/<int:pk>/', views.parking_place_delete, name='parking_place_delete'),
    
    # PaymentDetail URLs
    path('payment-details/', views.payment_detail_list, name='payment_detail_list'),
    
    # VehicleType URLs
    path('vehicle-types/', views.vehicle_type_list, name='vehicle_type_list'),
   
    # LogDetail URLs
    path('log-details/', views.log_detail_list, name='log_detail_list'),
   
]
