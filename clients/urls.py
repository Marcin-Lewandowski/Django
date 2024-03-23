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

]