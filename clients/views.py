# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



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
def search_rooms(request):
    return render(request, 'search_rooms.html', {'user': request.user})

@login_required
def special_offers(request):
    return render(request, 'special_offers.html', {'user': request.user})


@login_required
def submit_review(request):
    return render(request, 'submit_review.html', {'user': request.user})

@login_required
def account_settings(request):
    return render(request, 'account_settings.html', {'user': request.user})


def reservation_planning(request):
    base_template = 'base2.html' if request.user.is_authenticated else 'base.html'
    if request.method == 'POST':
        # Scal konteksty do jednego słownika
        context = {
            'base_template': base_template,
            'user': request.user
        }
        return render(request, 'reservation_planning.html', context)
    else:
        return HttpResponse("To żądanie powinno być metodą POST.")