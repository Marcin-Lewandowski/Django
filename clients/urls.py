from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView

from .views import ReservationPlanningAPIView


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirects logged in users
    success_url = reverse_lazy('user_profile')  # Redirected after successful login

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('profile/', views.user_profile, name='user_profile'),
    
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('reservation_planning/', views.reservation_planning, name='reservation_planning'),
    path('api/reservation-planning/', ReservationPlanningAPIView.as_view(), name='reservation-planning-api'),
]

