
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from datetime import timedelta, datetime, time
from django.db.models import Q
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length = 100)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Double'),
        ('double', 'Twin'),
        ('suite', 'Trio'),
        ('family', 'Family') 
    ]
    
    ROOM_NUMBERS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
]

    
    ROOM_CAPACITY = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    
    ROOM_BEDS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]
    
    number = models.CharField(max_length=10, unique=True, choices=ROOM_NUMBERS, verbose_name="Room number")
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name="Room type")
    capacity = models.IntegerField(choices=ROOM_CAPACITY, verbose_name="Capacity")
    beds = models.IntegerField(choices=ROOM_BEDS, verbose_name="Number of beds")
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price per night")
    available = models.BooleanField(default=True, verbose_name="Available")
    amenities = models.TextField(blank=True, verbose_name="Amenities")
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        if self.beds == 1:
            return f"Room No {self.number} - {self.get_room_type_display()} - {self.get_beds_display()} bed - Capacity {self.get_capacity_display()} "
        else:
            return f"Room No {self.number} - {self.get_room_type_display()} - {self.get_beds_display()} beds - Capacity {self.get_capacity_display()} "

   
        
        

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Payment pending'),
        ('cancelled', 'Payment canceled'),
    ]
    SERVICE_TYPE_CHOICES = [
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    ROOM_TYPES = [
        ('single', 'Double'),
        ('double', 'Twin'),
        ('suite', 'Trio'),
        ('family', 'Family') 
    ]
    ROOM_NUMBERS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ]
    
    GUESTS_NUMBERS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='reservations')

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name="Room type")
    room_number = models.CharField(max_length=10, unique=True, choices=ROOM_NUMBERS, verbose_name="Room number")
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    number_of_guests = models.IntegerField(choices=GUESTS_NUMBERS, verbose_name="Guests numbers")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES)
    check_in_out_verified = models.BooleanField(default=False)
    cancellation_deadline = models.DateTimeField(null=True, blank=True)
    confirmation_code = models.CharField(max_length=50, unique=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    customer_review = models.TextField(blank=True, null=True, verbose_name="Customer review")
    special_requests = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Room reservation for {self.user} - {self.room}: Number of guests - {self.number_of_guests} "

    def clean(self):
        # Checking if the start date is earlier than the end date
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError("The start date must be earlier than the end date.")


    def save(self, *args, **kwargs):
        self.full_clean()
        super(Reservation, self).save(*args, **kwargs)

   
CHECK_IN_HOUR = 14  # 14:00 or 2 PM
CHECK_OUT_HOUR = 11  # 11:00 AM

def adjust_check_in_date(date):
    """Adjusts the given date to the standard check-in time."""
    return datetime.combine(date, time(CHECK_IN_HOUR, 0))

def adjust_check_out_date(date):
    """Adjusts the given date to the standard check-out time."""
    return datetime.combine(date, time(CHECK_OUT_HOUR, 0)) 
   
   
   


def check_room_availability(start_date, end_date, number_of_guests):
    start_date = adjust_check_in_date(start_date)
    end_date = adjust_check_out_date(end_date)

    # We filter rooms that can accommodate the appropriate number of guests
    potential_rooms = Room.objects.filter(capacity__gte=number_of_guests)

    # We are looking for reservations that match the selected period
    conflicting_reservations = Reservation.objects.filter(
        room__in=potential_rooms,
        # We check for overlapping dates
        end_date__gt=adjust_check_in_date(start_date),  # Reservations that end after scheduled check-in
        start_date__lt=adjust_check_out_date(end_date),  # Reservations that start before your scheduled check-out
    
        status='confirmed'
    ).values_list('room', flat=True)

    # We exclude rooms with conflicting reservations
    available_rooms = potential_rooms.exclude(id__in=conflicting_reservations)

    return available_rooms