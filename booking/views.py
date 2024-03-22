from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rezerwacje(request):
    return HttpResponse("<h1> Rezerwacje </h1> <br> <h2> Robimy rezerwacje na hotel mordo </h2>")