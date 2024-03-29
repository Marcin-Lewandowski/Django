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
def submit_review(request):
    return render(request, 'submit_review.html', {'user': request.user})



def reservation_planning(request):
    base_template = 'base2.html' if request.user.is_authenticated else 'base.html'
    if request.method == 'POST':
        # Retrieving data from a form
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        
        # Adding form data to the context
        context = {
            'base_template': base_template,
            'user': request.user,
            'start_date': start_date,
            'end_date': end_date,
            'adults': adults,
            'children': children,
        }
        return render(request, 'reservation_planning.html', context)
    else:
        return HttpResponse("This request should be a POST method.")