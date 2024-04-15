from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Reservation, Hotel, Room
from .serializer import ReservationSerializer, HotelSerializer, RoomSerializer

# class ReservationViewSet(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer

class HotelListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Hotel items
        '''
        hotels = Hotel.objects.filter()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Hotel with given Hotel data
        '''
        data = {
            'hotel': request.data.get('hotel'), 
            'name': request.data.get('name'), 
        }
        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class HotelDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, hotel_id):
        '''
        Helper method to get the object with given hotel_id
        '''
        try:
            return Hotel.objects.get(id=hotel_id)
        except Hotel.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, hotel_id, *args, **kwargs):
        '''
        Retrieves the Hotel with given hotel_id
        '''
        hotel_instance = self.get_object(hotel_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with hotel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = HotelSerializer(hotel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, hotel_id, *args, **kwargs):
        '''
        Updates the hotel item with given hotel_id if exists
        '''
        hotel_instance = self.get_object(hotel_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with hotel id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'hotel': request.data.get('hotel'), 
            'name': request.data.get('name'), 
        }
        serializer = HotelSerializer(instance = hotel_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, hotel_id, *args, **kwargs):
        '''
        Deletes the hotel item with given hotel_id if exists
        '''
        hotel_instance = self.get_object(hotel_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with hotel id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        hotel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )    

class ReservationListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Reservation items
        '''
        hotels = Reservation.objects.filter()
        serializer = ReservationSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Reservation with given Reservation data
        '''
        data = {
            'reservation': request.data.get('reservation'), 
            # 'name': request.data.get('name'), 
        }
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class ReservationDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, reservation_id):
        '''
        Helper method to get the object with given reservation_id
        '''
        try:
            return Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, reservation_id, *args, **kwargs):
        '''
        Retrieves the Reservation with given reservation_id
        '''
        hotel_instance = self.get_object(reservation_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with reservation id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ReservationSerializer(hotel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, reservation_id, *args, **kwargs):
        '''
        Updates the reservation item with given reservation_id if exists
        '''
        hotel_instance = self.get_object(reservation_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with reservation id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'reservation': request.data.get('reservation'), 
            # 'name': request.data.get('name'), 
        }
        serializer = ReservationSerializer(instance = hotel_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, reservation_id, *args, **kwargs):
        '''
        Deletes the reservation item with given reservation_id if exists
        '''
        hotel_instance = self.get_object(reservation_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with reservation id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        hotel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )    


class RoomListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Room items
        '''
        hotels = Room.objects.filter()
        serializer = RoomSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Room with given Room data
        '''
        data = {
            'room': request.data.get('room'), 
            # 'name': request.data.get('name'), 
        }
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class RoomDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, room_id):
        '''
        Helper method to get the object with given room_id
        '''
        try:
            return Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, room_id, *args, **kwargs):
        '''
        Retrieves the Room with given room_id
        '''
        hotel_instance = self.get_object(room_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with room id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RoomSerializer(hotel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, room_id, *args, **kwargs):
        '''
        Updates the room item with given room_id if exists
        '''
        hotel_instance = self.get_object(room_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with room id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'room': request.data.get('room'), 
            # 'name': request.data.get('name'), 
        }
        serializer = RoomSerializer(instance = hotel_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, room_id, *args, **kwargs):
        '''
        Deletes the room item with given room_id if exists
        '''
        hotel_instance = self.get_object(room_id)
        if not hotel_instance:
            return Response(
                {"res": "Object with room id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        hotel_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )    


    