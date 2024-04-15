# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from hotel.models import check_room_availability
from django.utils.dateparse import parse_datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from hotel.models import Room
from hotel.serializers import RoomSerializer



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')



@login_required
def user_profile(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def my_reservations(request):
    return render(request, 'my_reservations.html', {'user': request.user})


@login_required
def submit_review(request):
    return render(request, 'submit_review.html', {'user': request.user})




# old function
def reservation_planning(request):
    base_template = 'base2.html' if request.user.is_authenticated else 'base.html'
    if request.method == 'POST':
        
        # Retrieving and converting data from the form
        start_date = parse_datetime(request.POST.get('start_date'))
        end_date = parse_datetime(request.POST.get('end_date'))
        adults = int(request.POST.get('adults', 0))  
        children = int(request.POST.get('children', 0))  
        
        number_of_guests = adults + children
        
        if start_date < end_date:
        
            # Checking room availability
            available_rooms = check_room_availability(start_date, end_date, number_of_guests)
            
            # Adding form data and available rooms to the context
            context = {
                'base_template': base_template,
                'user': request.user,
                'start_date': start_date,
                'end_date': end_date,
                'adults': adults,
                'children': children,
                'number_of_guests': number_of_guests,
                'available_rooms': available_rooms,
            }
            return render(request, 'reservation_planning.html', context)
        else:
            context = {
                'base_template': base_template,
                'user': request.user,
                'start_date': start_date,
                'end_date': end_date,
                'adults': adults,
                'children': children,
                'number_of_guests': number_of_guests,
            }
            return render(request, 'adjust_planning.html', context)
            
    else:
        return HttpResponse("This request should be a POST method.")
    
    
    
class ReservationPlanningAPIView(APIView):
    def post(self, request, *args, **kwargs):
        start_date = parse_datetime(request.POST.get('start_date'))
        end_date = parse_datetime(request.POST.get('end_date'))
        adults = int(request.POST.get('adults', 0))  
        children = int(request.POST.get('children', 0)) 
        
        if not start_date or not end_date:
            return Response({"error": "Invalid dates provided"}, status=400)
        
        if adults < 0 or children < 0:
            return Response({"error": "Number of adults or children cannot be negative"}, status=400)
        
        if start_date >= end_date:
            return Response({"error": "Start date must be before end date"}, status=400)
        
        
        number_of_guests = adults + children
        available_rooms = check_room_availability(start_date, end_date, number_of_guests)
        
        
        serializer = RoomSerializer(available_rooms, many=True)
        return Response(serializer.data)
            
    