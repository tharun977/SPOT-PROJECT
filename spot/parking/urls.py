from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # The root URL for homepage
    # User URLs
    path('users/', views.user_list, name='user_list'),
    path('users/view/<int:pk>/', views.user_view, name='user_view'),
    path('users/new/', views.user_create, name='user_new'),
    path('users/edit/<int:pk>/', views.user_update, name='user_edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    
    # ParkingPlace URLs
    path('parking-places/', views.parking_place_list, name='parking_place_list'),
    path('parking-places/new/', views.parking_place_create, name='parking_place_new'),
    path('parking-places/edit/<int:pk>/', views.parking_place_update, name='parking_place_edit'),
    path('parking-places/view/<int:pk>/', views.parking_place_view, name='parking_place_view'),
    path('parking-places/delete/<int:pk>/', views.parking_place_delete, name='parking_place_delete'),
    
    # PaymentDetail URLs
    path('payment-details/', views.payment_detail_list, name='payment_detail_list'),
    path('payment-detail/view/<int:pk>/', views.payment_detail_view, name='payment_detail_view'),
    path('payment-detail/edit/<int:pk>/', views.payment_detail_update, name='payment_detail_edit'),
    path('payment-detail/delete/<int:pk>/', views.payment_detail_delete, name='payment_detail_delete'),
    
    # VehicleType URLs
    path('vehicle-types/', views.vehicle_type_list, name='vehicle_type_list'),
    path('vehicle-type/new/', views.vehicle_type_create, name='vehicle_type_new'),
    path('vehicle-type/edit/<int:pk>/', views.vehicle_type_update, name='vehicle_type_edit'),
    path('vehicle-type/view/<int:pk>/', views.vehicle_type_view, name='vehicle_type_view'),
    path('vehicle-type/delete/<int:pk>/', views.vehicle_type_delete, name='vehicle_type_delete'),
    
    # LogDetail URLs
    path('log-details/', views.log_detail_list, name='log_detail_list'),
    path('log-detail/view/<int:pk>/', views.log_detail_view, name='log_detail_view'),
    path('log-detail/edit/<int:pk>/', views.log_detail_update, name='log_detail_edit'),
    path('log-detail/delete/<int:pk>/', views.log_detail_delete, name='log_detail_delete'),
]
