from django.urls import path
from .views import HotelList, HotelDetail, ReservationList, ReservationDetail, RoomList, RoomDetail

urlpatterns = [
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelDetail.as_view(), name='hotel-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
]
