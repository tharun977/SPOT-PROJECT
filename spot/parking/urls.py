from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('users/view/<int:pk>/', views.user_view, name='user_view'),
    path('users/new/', views.user_create, name='user_new'),
    path('users/edit/<int:pk>/', views.user_update, name='user_edit'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),

    # Define similar URLs for other models like ParkingPlace, PaymentDetail, etc.
]
