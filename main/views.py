from msilib.schema import ListView
from multiprocessing import context
from re import M, search, template
from unicodedata import decimal
from urllib import request
from django.shortcuts import render
from django.contrib import messages
from main.models import *
from .forms import *
from django.views.generic import ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.messages import constants
from django.db.models import Q


def index(request):
    
    menor_preco = Moto.objects.all().order_by('preco')[:4]
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
        'menor_preco' : menor_preco,
        'add_recente' : add_recente,       
        }

    search = request.GET.get('search')

    if search:
        moto_list = Moto.objects.filter(modelo__icontains=search)
        return render(request, 'motos.html', moto_list)
    return render(request, 'index.html', context)


def motos(request):
    
    #Inicio 
    motos = Moto.objects.all().order_by('-id')
    
    
    cont = 0
    ate10, mais10 = False, False
    honda = False
    yamaha = False
    c100 = False
    c125 = False 
    c150 = False 
    c160 =  False 
    c250 = False 
    c300 = False

    selectform = SelectForm(request.POST or None)
    checkboxform = CheckboxForm(request.POST or None)
    
    #Ver se é um request
    if request.method == "POST":

        #Ver qual dos forms é
        if 'selectBt' in request.POST:
            if selectform.is_valid():
                print('Sucesso')
                resposta = request.POST['selecao']
                if resposta == '1':
                    motos = Moto.objects.all().order_by('-id')
                if resposta == '2':
                    motos = Moto.objects.all().order_by('-preco')
                if resposta == '3':
                    motos = Moto.objects.all().order_by('preco')
        
        if 'checkboxBt' in request.POST:
            if checkboxform.is_valid():
                if request.POST.get("ate10", False):
                    ate10 = True
                    
                if request.POST.get("mais10", False):
                    mais10 = True

                if request.POST.get("honda", False):
                    honda = True
                    
                if request.POST.get("yamaha", False):
                    yamaha = True
                
                if request.POST.get("c100", False):
                    c100 = True
                
                if request.POST.get("c125", False):
                    c125 = True

                if request.POST.get("c150", False):
                    c150 = True
                
                if request.POST.get("c160", False):
                    c160 = True

                if request.POST.get("c250", False):
                    c250 = True

                if request.POST.get("c300", False):
                    c300 = True
                
                
                vetor = [ate10, mais10, honda, yamaha, c100, c125, c150, c160, c250, c300]
                print (f'O vetor é {vetor}')

                cont = vetor.count(True)
                print(cont)
                
                ate10 = Q(preco__lte=10000)
                mais10 = Q(preco__gte=10000)
                honda = Q(marca__icontains='honda')
                yamaha = Q(marca__icontains='yamaha')
                c100 = Q(cilindradas='100')
                c125 = Q(cilindradas='125') 
                c150 = Q(cilindradas='150') 
                c160 =  Q(cilindradas='160') 
                c250 = Q(cilindradas='250')
                c300 = Q(cilindradas='300')
                
                if cont == 1:
                    if request.POST.get("ate10", False):
                        motos = Moto.objects.all().filter(ate10)
                    
                    if request.POST.get("mais10", False):
                        motos = Moto.objects.all().filter(mais10)

                    if request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(honda)

                    if request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(yamaha)
                
                    if request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(c100)
                    
                    if request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(c125)

                    if request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(c150)
                
                    if request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c160)
                
                    if request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c250)

                    if request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c300)

                elif cont == 2:
                    print('Duas seleções')
                    
                    # Dois preços 
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False):
                        motos = Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)


                    # Duas marcas
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)

                    # Duas cilindradas
                    if request.POST.get("c100", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125)

                    if request.POST.get("c100", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c150)

                    if request.POST.get("c100", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c160)

                    if request.POST.get("c100", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c250)

                    if request.POST.get("c100", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c300)



                    # Um preco e uma marca
                    if request.POST.get("ate10", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha)

                    if request.POST.get("mais10", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha)

                    # Um preco e uma cilindrada
                    if request.POST.get("ate10", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c300)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c300)

                    # Uma marca e uma cilindrada
                    if request.POST.get("c100", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c100) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c125", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c125) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c150", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c150) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c160", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c160) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c250", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c250) & Moto.objects.all().filter(yamaha)

                    if request.POST.get("c300", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c300) & Moto.objects.all().filter(yamaha)

                    if request.POST.get("c100", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c100) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c125", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c125) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c150", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c150) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c160", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c160) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c250", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c250) & Moto.objects.all().filter(honda)

                    if request.POST.get("c300", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c300) & Moto.objects.all().filter(honda)
               
                elif cont == 3:
                    #Três cilidradas 
                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)
                    
                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c160)

                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c250)
                    
                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c300)
                    
                    if request.POST.get("c100", False) and request.POST.get("c150", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)

                    if request.POST.get("c100", False) and request.POST.get("c160", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)
                    
                    if request.POST.get("c100", False) and request.POST.get("c250", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)

                    if request.POST.get("c125", False) and request.POST.get("c150", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150) | Moto.objects.all().filter(c160)

                    if request.POST.get("c150", False) and request.POST.get("c160", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c150) | Moto.objects.all().filter(c160) | Moto.objects.all().filter(c250)
                    
                    if request.POST.get("c160", False) and request.POST.get("c250", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c160) | Moto.objects.all().filter(c250) | Moto.objects.all().filter(c300)


                    # Dois precos e uma marca
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("honda", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("yamaha", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(yamaha)

                    #Dois precos e uma cilindrada
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c100", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c125", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c150", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c160", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c250", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c300", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c300)


                    #Duas marcas e um preco 
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("ate10", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(ate10)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("mais10", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(mais10)

                    #duas marcas e uma cilindrada
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c100", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c125", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c150", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c160", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c250", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c300", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c300)


                    #Três diferentes 
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c125", False):
                        motos = (Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda)) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c160)

                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c300)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c160)

                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c300)
                    

                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c160)

                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c300)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c160)

                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c300)


                
#PAGINAÇÃO
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '12')
    
    if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '10'

    paginator = Paginator(motos, parametro_limit)
    # trata o erro de uma paginação que não existe
    try:
        page = paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)


#CONTEXT
    context = {'motos' : page,
    'checkboxform' : checkboxform,
    'selectform' : selectform,
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
        'checkboxform' : checkboxform,
        'selectform' : selectform,
        }
        return render(request, 'motos.html', cont)
    else:
        return render(request, 'motos.html', context)


def detalhes(request, id):
    moto = Moto.objects.get(id=id)
    menor_preco = Moto.objects.all().order_by('preco')[:4]
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
        'menor_preco' : menor_preco,
        'add_recente' : add_recente,
        'viewModal' : viewModal, 
        }
    
    return render(request, 'detalhes.html', context)

