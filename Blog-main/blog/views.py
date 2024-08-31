from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'blog/index.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def profissoes(request):
    lista_profissoes = profissoes.objects.all()
    context = {
        'profissoes': lista_profissoes
    }
    return render(request, 'blog/profissoes.html', context)

def passatempos(request):
    passatempos = Passatempos.objects.all()
    context = {
        'passatempos': passatempos
    }
    return render(request, 'blog/passatempos.html', context)
