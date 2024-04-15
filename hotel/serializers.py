from rest_framework import serializers
from .models import Room 

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['number', 'room_type', 'capacity', 'beds', 'price_per_night', 'amenities']
