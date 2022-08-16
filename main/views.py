from multiprocessing import context
from django.shortcuts import render
from main.models import *

def index(request):
    return render(request, 'index.html')

def motos(request):
    lista = Moto.objects.all()
    context = {'motos' : lista}
    return render(request, 'motos.html', context)

def detalhes(request):
    return render(request, 'detalhes.html')

