from msilib.schema import ListView
from multiprocessing import context
from re import M, search, template
from urllib import request
from django.shortcuts import render
from django.contrib import messages
from main.models import *
from .forms import *
from django.views.generic import ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.messages import constants



def index(request):
    
    menor_valor = Moto.objects.all().order_by('valor_vista')[:4]
    add_recente = Moto.objects.all().order_by('-id')[:4]

    form = ContatoForm(request.POST or None)

    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            print("Enviado com sucesso")
            messages.add_message(request, constants.SUCCESS, 'Mensagem enviada com sucesso')
            form = ContatoForm()
        else:
            print("Erro ao enviar email")
            

    context = {
        'form': form,
        'menor_valor' : menor_valor,
        'add_recente' : add_recente,        
        }



    search = request.GET.get('search')

    if search:
        moto_list = Moto.objects.filter(modelo__icontains=search)
        return render(request, 'motos.html', moto_list)
    return render(request, 'index.html', context)

def motos(request):
    
    add_recente = Moto.objects.all().order_by('-id')



#SELECT FILTRO
    select = request.POST.get('select')
    print(select)



#CHECKBOX FILTRO
    formFiltro = FiltrosForm(request.POST or None)
    if str(request.method) == 'POST':
        if formFiltro.is_valid():
            print("Enviado com sucesso")
            print(formFiltro)
            formFiltro = FiltrosForm()
        else:
            print("Erro ao enviar email")



#PAGINAÇÃO
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '10')
    
    if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '10'

    paginator = Paginator(add_recente, parametro_limit)
    # trata o erro de uma paginação que não existe
    try:
        page = paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)
    

#CONTEXT
    context = {'motos' : page,
    'formFiltro' : formFiltro,
    }

#BARRA DE PESQUISA
    search = request.GET.get('search')
    if search:
        lista_filter = Moto.objects.filter(modelo__icontains=search)
        paginator = Paginator(lista_filter, parametro_limit)
        try:
            page = paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = paginator.page(1)
    
        cont = {'motos' : page,
        'form' : formFiltro,
        }
        return render(request, 'motos.html', cont)
    else:
        return render(request, 'motos.html', context)



def detalhes(request, id):
    moto = Moto.objects.get(id=id)
    menor_valor = Moto.objects.all().order_by('valor_vista')[:4]
    add_recente = Moto.objects.all().order_by('-id')[:4]

    viewModal = False

    form = CompraForm(request.POST or None)
    
    search = request.GET.get('search') 
    if search:
        moto_list = Moto.objects.filter(modelo__icontains=search)
        return render(request, 'motos.html', moto_list)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            viewModal = True
            form.send_mail()
            print("Enviado com sucesso")
            messages.success(request, 'Profile details updated.')
            form = CompraForm()

        else:
            print("Erro ao enviar email")

    context = {
        'moto' : moto,
        'form' : form,
        'menor_valor' : menor_valor,
        'add_recente' : add_recente,
        'viewModal' : viewModal, 
        }
    
    return render(request, 'detalhes.html', context)

