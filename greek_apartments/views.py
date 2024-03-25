from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    base_template = 'base2.html' if request.user.is_authenticated else 'base.html'
    return render(request, 'index.html', {'base_template': base_template})

def about(request):
    base_template = 'base2.html' if request.user.is_authenticated else 'base.html'
    return render(request, 'about.html', {'base_template': base_template})




def contact(request):
    base_template = 'base2.html' if request.user.is_authenticated else 'base.html'
    return render(request, 'contact.html', {'base_template': base_template})
