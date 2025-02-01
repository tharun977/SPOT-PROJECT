from django.urls import path
from . import views

urlpatterns = [
    path('', views.parking_slot_list, name='parking_list'),
    path('view/<int:pk>/', views.parking_slot_view, name='parking_view'),
    path('new/', views.parking_slot_create, name='parking_new'),
    path('edit/<int:pk>/', views.parking_slot_update, name='parking_edit'),
    path('delete/<int:pk>/', views.parking_slot_delete, name='parking_delete'),
]
