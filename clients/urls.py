from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', views.user_profile, name='profile'),

]