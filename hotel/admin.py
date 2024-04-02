from django.contrib import admin
from .models import Reservation, Room


admin.site.register(Room)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room', 'number_of_guests', 'start_date', 'end_date', 'status')

