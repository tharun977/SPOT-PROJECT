from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParkingSlotList.as_view(), name='parking_list'),
    path('view/<int:pk>/', views.ParkingSlotDetail.as_view(), name='parking_view'),
    path('new/', views.ParkingSlotCreate.as_view(), name='parking_new'),
    path('edit/<int:pk>/', views.ParkingSlotUpdate.as_view(), name='parking_edit'),
    path('delete/<int:pk>/', views.ParkingSlotDelete.as_view(), name='parking_delete'),
]
