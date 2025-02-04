from django.urls import path
from . import views
from .views import user_login, register

urlpatterns = [
    # Authentication URLs
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path('', views.user_login, name='user_login'),
    path('homepage/', views.homepage, name='homepage'),  # Ensure consistent URL structure

    # User URLs
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/edit/<int:pk>/', views.user_update, name='user_edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),

    # Parking Place URLs
    path('parking-places/', views.parking_place_list, name='parking_place_list'),
    path('parking-places/create/', views.parking_place_create, name='parking_place_create'),
    path('parking-places/view/<int:pk>/', views.parking_place_view, name='parking_place_view'),
    path('parking-places/delete/<int:pk>/', views.parking_place_delete, name='parking_place_delete'),

    # Parking Lot URLs (if applicable)
    path('parking-lots/', views.parking_lot_list, name='parking_lot_list'),
    path('parking-lots/create/', views.parking_lot_create, name='parking_lot_create'),
    path('parking-lots/edit/<int:pk>/', views.parking_lot_update, name='parking_lot_edit'),
    path('parking-lots/delete/<int:pk>/', views.parking_lot_delete, name='parking_lot_delete'),

    # Payment Detail URLs
    path('payment-details/', views.payment_detail_list, name='payment_detail_list'),
    path('payment-details/view/<int:pk>/', views.payment_detail_view, name='payment_detail_view'),

    # Vehicle Type URLs
    path('vehicle-types/', views.vehicle_type_list, name='vehicle_type_list'),
    path('vehicle-types/create/', views.vehicle_type_create, name='vehicle_type_create'),
    path('vehicle-types/delete/<int:pk>/', views.vehicle_type_delete, name='vehicle_type_delete'),

    # Log Detail URLs
    path('log-details/', views.log_detail_list, name='log_detail_list'),
    path('log-details/view/<int:pk>/', views.log_detail_view, name='log_detail_view'),
]

