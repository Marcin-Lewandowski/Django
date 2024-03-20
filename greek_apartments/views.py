from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    return HttpResponse("<h1>Witaj</h1>")

def rezerwacje(request):
    return HttpResponse("<h1> Rezerwacje </h1> <br> <h2> Robimy stronke mordo </h2>")