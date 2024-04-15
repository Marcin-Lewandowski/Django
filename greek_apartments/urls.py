"""
URL configuration for greek_apartments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from clients.views import reservation_planning, user_profile
from clients.views import ReservationPlanningAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', user_profile, name='user_profile'),
    path('booking/', include('booking.urls')),
    path('clients/', include('clients.urls')),
    path('reservation_planning/', reservation_planning, name='reservation_planning'),
    path('api/reservation-planning/', ReservationPlanningAPIView.as_view(), name='reservation-planning-api'),
]