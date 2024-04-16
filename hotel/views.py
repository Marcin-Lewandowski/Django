from rest_framework import generics, permissions
from .models import Hotel, Reservation, Room
from .serializer import HotelSerializer, ReservationSerializer, RoomSerializer

# Bazowa klasa dla APIView z często używanymi metodami
class BaseView:
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            return None

# Widoki dla Hotel
class HotelList(generics.ListCreateAPIView, BaseView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView, BaseView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

# Widoki dla Reservation
class ReservationList(generics.ListCreateAPIView, BaseView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView, BaseView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Widoki dla Room
class RoomList(generics.ListCreateAPIView, BaseView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView, BaseView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
