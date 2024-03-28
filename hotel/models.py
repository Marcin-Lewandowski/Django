
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()


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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='reservations')

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    room_type = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    number_of_guests = models.IntegerField()
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

   