from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HotelListApiView,
    HotelDetailApiView,
    ReservationListApiView,
    ReservationDetailApiView,
    RoomListApiView,
    RoomDetailApiView,
)

urlpatterns = [
    path('hotels/', HotelListApiView.as_view(), name='hotel-list'),
    path('hotels/<int:hotel_id>/', HotelDetailApiView.as_view(), name='hotel-detail'),
    
    path('reservations/', ReservationListApiView.as_view(), name='reservation-list'),
    path('reservations/<int:reservation_id>/', ReservationDetailApiView.as_view(), name='reservation-detail'),

    path('rooms/', RoomListApiView.as_view(), name='room-list'),
    path('rooms/<int:room_id>/', RoomDetailApiView.as_view(), name='room-detail'),
]
