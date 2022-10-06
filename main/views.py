from msilib.schema import ListView
from multiprocessing import context
from re import M, search, template
from django.shortcuts import render
from django.contrib import messages
from main.models import *
from .forms import *
from django.views.generic import ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage



def index(request):
    form = ContatoForm(request.POST or None)
        
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            print("Enviado com sucesso")
            form = ContatoForm()
        else:
            print("Erro ao enviar email")

    context = {'form': form}

    search = request.GET.get('search')
    if search:
        lista = Moto.objects.filter(modelo__icontains=search)
        cont2 = {'motos': lista}
        return render(request,'motos.html', cont2)

    return render(request, 'index.html', context)

def motos(request):
    template_name = 'motos.html'
    moto_list = Moto.objects.all()
    search = request.GET.get('search')
    
    paginator = Paginator(moto_list, 4)
    
    page = request.GET.get('page')

    motos = paginator.get_page(page)

    if search:
        moto_list = Moto.objects.filter(modelo__icontains=search)



    return render(request, template_name, {'motos' : motos})


def detalhes(request, id):
    moto = Moto.objects.get(id=id)
    context = {'moto' : moto}
    
    search = request.GET.get('search')
    if search:
        lista = Moto.objects.filter(modelo__icontains=search)
        cont2 = {'motos': lista}
        return render(request,'motos.html', cont2)
    else:
        return render(request, 'detalhes.html', context)

