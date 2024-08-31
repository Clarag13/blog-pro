from django.shortcuts import render
from .models import Hobbies, SeriesFavoritas

def index(request):
    return render(request, 'blog/index.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def hobbies(request):
    lista_hobbies = Hobbies.objects.all()
    context = {
        'hobbies': lista_hobbies
    }
    return render(request, 'blog/hobbies.html', context)

def series(request):
    series = SeriesFavoritas.objects.all()
    context = {
        'series': series
    }
    return render(request, 'blog/series.html', context)
