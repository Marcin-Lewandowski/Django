from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Przekierowuje zalogowanych użytkowników
    success_url = reverse_lazy('user_profile')  # Przekierowanie po pomyślnym zalogowaniu

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.user_profile, name='user_profile'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('search_rooms/', views.search_rooms, name='search_rooms'),
    path('special_offers/', views.special_offers, name='special_offers'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('reservation_planning/', views.reservation_planning, name='reservation_planning'),
]